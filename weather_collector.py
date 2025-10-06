"""
weather_collector.py
--------------------

🌤️ Simple Weather Data Collector ⛈

This script:
1. Fetches current weather data from OpenWeatherMap API
2. Saves it to an SQLite database using functinos from database.py
3. Has to be run manually. (Set some reminders! ⏲️)
"""

import os
import requests
# import sqlite3
from config import BELGIAN_CITIES
from datetime import datetime
from dotenv import load_dotenv

# import local modules
from config import BELGIAN_CITIES
from database import setup_database, save_weather

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')


def get_weather(city):
    """
    Fetches current weather data from OpenWeatherMap API for 1 city.

    Returns Dictionary with weather data, None if request fails.
    """
    url = "http://api.openweathermap.org/data/2.5/weather" # API endpoint

    # API parameters we'll be sending
    # docs: https://openweathermap.org/current
    params = {
        'q': f'{city},BE',
        'appid': API_KEY,
        'units': 'metric'
    }

    try:
        # docs: https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
        response = requests.get(url, params=params, timeout=10)
        print(f"Status code: {response.status_code}")
        print(f"URL called: {response.url}")
        data = response.json()

        # Extract selected data
        # docs: https://openweathermap.org/current#fields_json
        weather_data = {
            'city': city,
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
            'wind_speed': data['wind']['speed'],
            'collected_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        return weather_data

    except Exception as error:
        # if anything goes wrong, print error and return None
        print(f"Error getting weather for {city}: {error}")
        return None

    
def main():
    """
    Main function - collects weather for all cities and stores in database.
    """
    print("\n" + "="*50)
    print(f"Starting weather collection at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*50 + "\n")

    # Make sure database table exists
    setup_database()

    # Track how many cities we successfully collected
    successful = 0

    # Loop through each city in our list
    for city in BELGIAN_CITIES:
        print(f"Getting weather for {city}...", end=" ")

        # Fetch weather data from API
        weather_data = get_weather(city)

        if weather_data:
            # Save to database using database.py
            save_weather(weather_data)
            successful += 1

            # Show what is collected
            temp = weather_data['temperature']
            desc = weather_data['description']
            print(f">>> {temp}°C", {desc})
        else:
            print(">>> Failed...")

    print(f"\nDone! Collected data for {successful}/{len(BELGIAN_CITIES)} cities")
    print("="*50 + "\n")

# This runs when you execute the script
# Checks for valid API_KEY
if __name__ == "__main__":
    if not API_KEY:
        print("ERROR: No API key found!")
        print("Make sure you have an .env file with OPENWEATHER_API_KEY=<your_key>")
    else:
        main()