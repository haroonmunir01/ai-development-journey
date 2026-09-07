import requests

def get_weather(city, country):
    name = f"{city},{country}"


    url = "https://api.open-meteo.com/v1/forecast"
    geocode_url = "https://geocoding-api.open-meteo.com/v1/search"

    try:
        params = {
            "name": name
        }

        response = requests.get(
            geocode_url,
            params=params,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        if not data.get("results"):
            return None

        lat = data["results"][0]["latitude"]
        long = data["results"][0]["longitude"]

    except requests.RequestException as e:
        return {"error": f"API request failed: {e}"}

    try:
        params = {
            "latitude": lat,
            "longitude": long,
            "current": "temperature_2m",
            "timezone": "auto"
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()
        data = response.json()

        return {
            "latitude": data["latitude"],
            "longitude": data["longitude"],
            "time": data["current"]["time"],
            "temperature": data["current"]["temperature_2m"]
        }

    except requests.RequestException as e:
        return {"error": f"API request failed: {e}"}

