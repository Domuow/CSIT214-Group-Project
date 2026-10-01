from pathlib import Path
import sqlite3
from datetime import date, datetime


DATABASE_PATH = Path(__file__).with_name("facilities.db")

# Establish a connection to the SQLite database and set up the row factory to return rows as dictionaries. This allows for easier access to column values by name rather than by index.
def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON") # Enforces foreign key constraints in SQLite, ensuring that relationships between tables are maintained correctly.
    return connection


def init_db():
    with get_connection() as connection:
        connection.executescript(
            """
            CREATE TABLE IF NOT EXISTS facilities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                description TEXT NOT NULL,
                capacity INTEGER NOT NULL DEFAULT 1 CHECK (capacity > 0)
            );

            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                facility_id INTEGER NOT NULL REFERENCES facilities(id),
                booking_date TEXT NOT NULL,
                start_time TEXT NOT NULL,
                end_time TEXT NOT NULL,
                booker_name TEXT NOT NULL,
                booker_email TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
                CHECK (start_time < end_time)
            );

            CREATE INDEX IF NOT EXISTS idx_bookings_facility_date
                ON bookings (facility_id, booking_date);
            """
        )
        add_facilities(connection)


def add_facilities(connection):
    # Added placeholder facilities to the database for testing purposes (THEY MAY NOT REFLECT ACTUAL FACILITIES AS OUTLINE BY PROJECT DESCRIPTION)
    # These can be modified or removed as needed.
    facilities = [
        ("Community Hall", "A flexible hall for meetings, classes and community events.", 120),
        ("Sports Court", "An indoor court suitable for basketball, volleyball and futsal.", 40),
        ("Meeting Room", "A quiet room for small meetings, workshops and study groups.", 12),
        ("Pickle Ball Equipment", "A set of pickleball equipment available for use in the sports court.", 4),
    ]
    connection.executemany(
        """
        INSERT OR IGNORE INTO facilities (name, description, capacity)
        VALUES (?, ?, ?)
        """,
        facilities,
    )


