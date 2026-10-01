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

# Add placeholder facilities to the database for testing purposes
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

def valid_booking_values(booking_date, start_time, end_time):
    try:
        requested_date = date.fromisoformat(booking_date)
        start = datetime.strptime(start_time, "%H:%M").time()
        end = datetime.strptime(end_time, "%H:%M").time()
    except (TypeError, ValueError):
        return None

    if requested_date < date.today() or start >= end:
        return None
    return requested_date, start, end

# Retrieves all facilities from the database (if none are specified) or filters them based on availability for a given date and time range
def get_facilities(booking_date=None, start_time=None, end_time=None):
    with get_connection() as connection:
        facilities = connection.execute(
            "SELECT id, name, description, capacity FROM facilities ORDER BY name"
        ).fetchall()

        # If no date and time are provided, return all facilities without filtering
        if not all((booking_date, start_time, end_time)):
            return facilities

        # Check if the provided date and time values are valid, and if not, return an empty list
        values = valid_booking_values(booking_date, start_time, end_time)
        if values is None:
            return []

        # Filter the facilities based on availability for the given date and time range
        requested_date, _, _ = values # Unpack the validated date and time values, ignoring the start and end times since they are not needed for the availability check
        available = []

        # Check for conflicts in bookings for each facility and add available facilities to the list
        for facility in facilities:
            conflict = connection.execute(
                """
                SELECT 1 FROM bookings
                WHERE facility_id = ?
                    AND booking_date = ?
                    AND start_time < ?
                    AND end_time > ?
                LIMIT 1
                """,
                (facility["id"], requested_date.isoformat(), end_time, start_time),
            ).fetchone() 
            # If a conflict is found (i.e., there is an existing booking that overlaps with the requested time), the facility will not be added to the available list. If no conflict is found, the facility is considered available and added to the list.
            if conflict is None:
                available.append(facility)
        # Return the list of available facilities that do not have any conflicting bookings for the specified date and time range
        return available 

