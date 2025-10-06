"""
database.py
-----------
Handels all database operations for th weather collector.

This file contains all the functions that interact with SQLite
- Creating database table
- Inserting weather data
- Retrieving data for analysis
"""

import sqlite3  # https://docs.python.org/3/library/sqlite3.html
from datetime import datetime

def setup_database():
    """
    Creates the weather database table if it doesn't exist yet.

    This function is safe to run multiple times. Of the table already exists, it won't overwrite or create a duplicate.
    """
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            temperature REAL,
            feels_like REAL,
            humidity INTEGER,
            description TEXT,
            wind_speed REAL,
            collected_at TEXT
        )
    ''')

    conn.commit()
    conn.close()


def save_weather(weather_data):
    """
    Saves one weather record to the database.
    
    Args:
        weather_data: dict containing weather information (per city)

    Example:
        weather_data = {
            'city': 'Brussels',
            'temperature': 15.5,
            'feels_like': 14.2,
            'humidity': 80,
            'description': 'light rain',
            'wind_speed': 5.2,
            'collected_at': '2025-10-02 18:30:00'
        }
    """
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO weather (city, temperature, feels_like, humidity,
                            description, wind_speed, collected_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        weather_data['city'],
        weather_data['temperature'],
        weather_data['feels_like'],
        weather_data['humidity'],
        weather_data['description'],
        weather_data['wind_speed'],
        weather_data['collected_at'],
    ))

    conn.commit()
    conn.close()

# The following functions are for checking the database:
# get_recent_data()
# count_records()
# They're not used as main functions.

def get_recent_data(limit=10):
    """
    Retrieves the most recent weather records from the data base
    
    Args:
        limit: number of records to retrieve (default: 10)

    Returns:
        List of tuples, each containing one weather record
    """
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT city, temperature, description, collect_at
        FROM weather
        ORDER BY collected_at DESC
        LIMIT ?
    ''', (limit,))

    rows = cursor.fetchall()
    conn.close()

    return rows

def count_records():
    """
    Counts total number of weather records in database.

    Returns:
        Integer: total number of records
    """
    conn = sqlite3.connect('weather.db')
    cursor = conn.cursor()

    cursor.execute('SELECT COUNT(*) FROM weather')
    count = cursor.fetchone()[0]

    conn.close()
    return count

# This runs if you execute this file directly (for testing)
if __name__ == "__main__":
    setup_database()
    print("Database setup complete")

    # Show current stats
    total = count_records()
    print(f"Total records in database: {total}")

    if total > 0:
        print("\nMost recent records:")
        recent = get_recent_data(5)
        for record in recent:
            print(f"{record[0]}: {record[1]}°C = {record[2]} ({record[3]})")