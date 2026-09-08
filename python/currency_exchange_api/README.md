# Currency Converter

## Overview

A Python currency conversion application that retrieves live exchange rates from the Frankfurter API and provides a Tkinter graphical interface for converting currencies.

The application also retrieves the available currencies from the API and dynamically populates the From and To dropdown menus.

## Features

* Enter an amount to convert
* Select the source currency from a dropdown
* Select the target currency from a dropdown
* Retrieve exchange rates through an API
* Dynamically load available currencies
* Validate user input
* Handle invalid amounts
* Prevent conversion between the same currency
* Handle API request errors
* Display the converted amount through the GUI

## Technologies

* Python
* Tkinter
* Requests
* JSON
* Frankfurter API

## Project Structure

```text
currency_api/
├── main.py
├── gui.py
└── README.md
```

## How It Works

```text
User
 ↓
Tkinter GUI
 ↓
User enters amount and selects currencies
 ↓
Input validation
 ↓
Frankfurter API
 ↓
Exchange rate
 ↓
Amount × Exchange Rate
 ↓
Converted result displayed
```

The application uses one API endpoint to retrieve exchange rates and another endpoint to retrieve the available currencies.

## API

This project uses the Frankfurter API for exchange-rate data.

The application sends the selected source and target currencies to the API, retrieves the exchange rate, and multiplies it by the amount entered by the user.

## Learning Objectives

This project was built to practice:

* Working with multiple APIs
* Sending GET requests with query parameters
* Processing JSON responses
* Extracting data from nested Python structures
* Working with dates
* Building dynamic Tkinter dropdowns
* Connecting GUI inputs to backend functions
* Input validation
* API error handling
* Separating GUI and API logic

## Purpose

This project is part of my AI Development Journey and focuses on strengthening practical Python and API development skills before moving toward LLM APIs and AI application development.
