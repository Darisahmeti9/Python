# BMI Calculator - Complete Program

print("=== BMI CALCULATOR ===")

while True:
    print("\nEnter Person Information:")

    name = input("Name: ")
    age = input("Age: ")
    height = float(input("Height (in meters): "))
    weight = float(input("Weight (in kilograms): "))

    # BMI Calculation
    bmi = weight / (height ** 2)

    # BMI Status
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 25:
        status = "Normal weight"
    elif 25 <= bmi < 30:
        status = "Overweight"
    else:
        status = "Obese"

    # Output
    print("\n--- BMI RESULT ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Height: {height} m")
    print(f"Weight: {weight} kg")
    print(f"BMI: {bmi:.2f}")
    print(f"Status: {status}")

    # Add another person option
    choice = input("\nDo you want to add another person? (yes/no): ").lower()
    if choice != "yes":
        print("\nThank you for using the BMI Calculator!")
        break
