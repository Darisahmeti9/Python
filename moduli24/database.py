import sqlite3
from models import Movie , MovieCreate

def create_conection():
    """Create a database connection"""
    connection =  sqlite3.connect("movie.db")
    connection.row_factory = sqlite3.Row
    return connection

