# Weather Data Collector -- WORK IN PROGRESS -- won't work yet

A simple Python project that collects real-time weather data for Belgian cities and stores it in a SQLite database.

## What it does

This script fetches current weather data from the OpenWeatherMap API every time it runs and saves the result to a local database. For now, the script has to be run manually, and I use reminders (⏲️) for when I should run the programme.

The goal is to build up a dataset over a few weeks that I can then analyse for patterns, trends, and practice with.

## Why I built this

Hands-on experience with:
- Working with REST APIs
- Database operations (creating tables, inserting data, querying)
- ETL concepts (Extract, Transform, Load)
- Building something I can actually use for a future project.

## Project structure
```zsh
weather-collector/
├── weather_collector.py   # Main script - fetches and stores weather data
├── database.py            # Database functions (setup, insert, query)
├── config.py              # Configuration (list of cities to track)
├── requirements.txt       # Python dependencies
├── .env                   # API key (not in repo - you'll need to create this)
├── .gitignore            
├── README.md              # This file
└── *weather.db*           # database will be created once the programme is run for the first time
```

## What each file does
**TODO:** explain what each file does.


## Tech stack
**TODO:** explain technologies used

## Setup instructions (At this time, it will not work yet!)

1. **Clone repo**
```zsh
git clone <link-repo> # add repo link
cd weather-collector
```
*Optional:*
```zsh
python3 -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

2. Install dependencies
```zsh
pip install -r requirements.txt
```
## Get your free API key
1. Go to [OpenWeatherMap](https://openweathermap.org))
2. Sign up for a free account
3. Go to you API keys section
4. Copy your API key
5. Create ```.env``` file:
    `OPENWEATHER_API_KEY=your_api_key_here```
    **important: never commit this file to Github. It's already in .gitignore**
6. Run the collector:
    ```python3 weather_collector.py```


## How to use it
**TODO:** Explain how I use it.

## Querying
**TODO:** explain some basic queries.

## Database functions
**TODO:** explain database and learnings.
**TODO:** Expalin database schema

## Next Steps
**TODO:** next steps

## API information
This project uses the [OpenWeatherMap Current Weather Data API](https://openweathermap.org/current)

## Troubleshooting
**TODO:** explain error messages here, and possible fixes.

## Contributing

This is a personal project, but if you spot bugs or have suggestions, freel free to open an issue.

## License
MIT License. Feel free to use this for your own learning.


---

*This is a learning project created as part of my transition into data science. Feedback welcome!*