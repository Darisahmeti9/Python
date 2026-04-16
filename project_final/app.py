import streamlit as st
import pandas as pd
from datetime import datetime
from database import get_connection, create_tables

create_tables()
conn = get_connection()

st.title("Hotel Management System")

menu = st.sidebar.selectbox(
    "Menu",
    ["View Rooms", "Add Guest", "Book Room", "Checkout", "Statistics"]
)

# View rooms
if menu == "View Rooms":
    rooms = pd.read_sql_query("SELECT * FROM rooms", conn)
    st.dataframe(rooms)

# Add guest
elif menu == "Add Guest":
    name = st.text_input("Guest Name")
    phone = st.text_input("Phone")

    if st.button("Save Guest"):
        conn.execute(
            "INSERT INTO guests (full_name, phone) VALUES (?, ?)",
            (name, phone)
        )
        conn.commit()
        st.success("Guest added successfully")

# Book room
elif menu == "Book Room":
    guests = pd.read_sql_query("SELECT * FROM guests", conn)
    rooms = pd.read_sql_query("SELECT * FROM rooms WHERE status='Available'", conn)

    guest_id = st.selectbox("Select Guest", guests["id"])
    room_id = st.selectbox("Select Room", rooms["id"])
    check_in = st.date_input("Check In")
    check_out = st.date_input("Check Out")

    if st.button("Book"):
        conn.execute("""
        INSERT INTO bookings (guest_id, room_id, check_in, check_out)
        VALUES (?, ?, ?, ?)
        """, (guest_id, room_id, str(check_in), str(check_out)))

        conn.execute("UPDATE rooms SET status='Booked' WHERE id=?", (room_id,))
        conn.commit()
        st.success("Room booked successfully")

# Checkout automatic + invoice
elif menu == "Checkout":
    bookings = pd.read_sql_query("""
    SELECT bookings.id, guests.full_name, rooms.room_number, rooms.price,
           bookings.check_in, bookings.check_out
    FROM bookings
    JOIN guests ON bookings.guest_id = guests.id
    JOIN rooms ON bookings.room_id = rooms.id
    """, conn)

    st.dataframe(bookings)

    booking_id = st.number_input("Booking ID", min_value=1)

    if st.button("Checkout Guest"):
        booking = conn.execute("""
        SELECT bookings.*, rooms.price, rooms.id as room_id
        FROM bookings
        JOIN rooms ON bookings.room_id = rooms.id
        WHERE bookings.id=?
        """, (booking_id,)).fetchone()

        if booking:
            check_in = datetime.strptime(booking["check_in"], "%Y-%m-%d")
            check_out = datetime.strptime(booking["check_out"], "%Y-%m-%d")

            days = (check_out - check_in).days
            total = days * booking["price"]

            conn.execute("""
            INSERT INTO invoices (booking_id, total_price, payment_status)
            VALUES (?, ?, ?)
            """, (booking_id, total, "Paid"))

            conn.execute("UPDATE rooms SET status='Available' WHERE id=?",
                         (booking["room_id"],))

            conn.execute("DELETE FROM bookings WHERE id=?", (booking_id,))
            conn.commit()

            st.success(f"Checkout complete. Total invoice: €{total}")

# Monthly statistics
elif menu == "Statistics":
    st.subheader("Monthly Hotel Statistics")

    bookings_stats = pd.read_sql_query("""
    SELECT substr(check_in,1,7) as month,
           COUNT(*) as total_bookings
    FROM bookings
    GROUP BY month
    """, conn)

    income_stats = pd.read_sql_query("""
    SELECT invoices.id,
           invoices.total_price
    FROM invoices
    """, conn)

    st.write("Bookings per month")
    st.dataframe(bookings_stats)

    st.write("Invoices")
    st.dataframe(income_stats)