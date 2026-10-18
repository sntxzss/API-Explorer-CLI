# API Explorer CLI

A command-line application for exploring and testing various APIs including weather, jokes, and keeping a history of requests.

## Features

- **Weather**: Get current weather information for any city using Open-Meteo API
- **Jokes**: Fetch random jokes from the Official Joke API
- **History**: View the last 10 API requests made during the session
- **Error Handling**: User-friendly error messages for connection issues and server errors

## Installation

1. Clone the repository or navigate to the project directory
2. Install required dependencies:
```bash
pip install httpx
```

## Usage

Run the application:
```bash
python explorer.py
```

### Menu Options

**1. Weather**
- Enter a city name to get current weather information
- Displays temperature (°C) and wind speed (km/h)
- Shows "Місто не знайдено" if the city doesn't exist

**2. Joke**
- Get a random joke
- View the setup and choose to see the punchline
- Jokes are saved to history

**3. History**
- View the last 10 API requests
- Shows request type, query, result, and timestamp

**0. Exit**
- Close the application

## Project Structure

### Files

- **explorer.py**: Main menu and user interface
- **jokes_api.py**: Handles requests to the Official Joke API
- **weather_api.py**: Handles weather requests using Open-Meteo geocoding and forecast APIs
- **history.py**: Manages saving and retrieving request history
- **history.json**: Stores historical API requests

### API Modules

#### jokes_api.py
- `get_joke()` → tuple[setup, punchline] or dict with error
- Returns a tuple with joke setup and punchline on success
- Returns dict with "error" key on failure

#### weather_api.py
- `get_forecast(city: str)` → dict or dict with error
- Uses Open-Meteo geocoding API to find city coordinates
- Fetches weather data for those coordinates
- Returns temperature and wind speed

#### history.py
- `save_history(type, query, result)`: Save a request to history.json
- `get_history()`: Retrieve the last 10 requests

## Error Handling

The application handles common errors gracefully:

- **No connection**: "No connection" message when unable to reach the API
- **Server error**: "Server error" message for HTTP failures
- **City not found**: "Місто не знайдено" when weather city doesn't exist

## Dependencies

- **httpx**: HTTP client for making API requests
- **json**: Built-in module for handling JSON data
- **datetime**: Built-in module for timestamps

## APIs Used

1. **Official Joke API**: https://official-joke-api.appspot.com/
2. **Open-Meteo**: https://open-meteo.com/
   - Geocoding API
   - Weather Forecast API
