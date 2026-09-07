# Weather API GUI

A simple Python weather application built to practice working with REST APIs, JSON responses, API error handling, and a basic graphical user interface using Tkinter.

## Features

* Accepts city and country from the user
* Uses a geocoding API to find latitude and longitude
* Uses a weather API to retrieve the current temperature
* Displays the current local time and temperature
* Handles invalid cities
* Handles API request errors
* Provides a simple Tkinter GUI

## Technologies

* Python
* Requests
* Tkinter
* Open-Meteo Geocoding API
* Open-Meteo Weather API
* JSON

## How It Works

```text
User
 ↓
Enter City + Country
 ↓
Tkinter GUI
 ↓
Geocoding API
 ↓
Latitude + Longitude
 ↓
Weather API
 ↓
Current Temperature + Time
 ↓
Display Result
```

## Project Structure

```text
weather_api/
├── main.py
├── gui.py
└── README.md
```

### `main.py`

Contains the API logic:

* Sends requests to the Open-Meteo Geocoding API
* Retrieves latitude and longitude
* Sends a request to the Open-Meteo Weather API
* Extracts the current temperature and time
* Handles API errors

### `gui.py`

Contains the graphical interface:

* City input
* Country input
* Get Weather button
* Weather result display
* Calls the API function from `main.py`

## Example

```text
Enter city:
Karachi

Enter country:
Pakistan

Location: Karachi, Pakistan
Time: 2026-09-07T18:00
Temperature: 29.4 °C
```

## What I Learned

This project was built as practical API development practice. It helped me understand:

* How REST APIs work
* API endpoints
* HTTP GET requests
* Query parameters
* JSON responses
* Nested dictionaries and lists
* Extracting data from API responses
* HTTP status codes
* Error handling with `try` and `except`
* Using `requests`
* Connecting API logic with a GUI
* Passing data between Python functions and files
* Using environment-independent application logic

## APIs Used

The application uses Open-Meteo's Geocoding API to convert a city name into coordinates and its Weather API to retrieve weather information.

## Purpose

This is a learning project and part of my journey toward AI and LLM application development.

The main goal was not to build a complex weather application, but to understand the fundamentals of integrating external APIs into Python applications.
