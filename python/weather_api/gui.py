import tkinter as tk
from main import get_weather

def handle_weather():
    city = city_entry.get()
    country = country_entry.get()


    result = get_weather(city, country)

    if result is None:
        result_label.config(text="City not found.")
    elif "error" in result:
        result_label.config(text=result["error"])
    else:
        result_label.config(
            text=f"Location: {city}, {country}\n"
                f"Time: {result['time']}\n"
                f"Temperature: {result['temperature']} °C"
        )


window = tk.Tk()
window.title("Weather App")
window.geometry("400x300")

city_label = tk.Label(window, text="Enter city:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

country_label = tk.Label(window, text="Enter country:")
country_label.pack()

country_entry = tk.Entry(window)
country_entry.pack()

get_weather_button = tk.Button(
    window,
    text="Get Weather",
    command=handle_weather
)
get_weather_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
