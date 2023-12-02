import requests

def fetch_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "appid": api_key,
        "units": "metric"  # For Fahrenheit use "imperial"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise HTTP errors if any
        return response.json()
    except requests.RequestException as e:
        print("Error fetching weather data:", e)
        return None
    except ValueError as e:
        print("Error decoding JSON:", e)
        return None

def display_weather_data(data):
    if not data:
        print("No weather data available.")
        return

    name = data.get("name")
    country = data.get("sys", {}).get("country")
    main_data = data.get("main")
    weather = data.get("weather", [{}])[0]

    if name and country and main_data and weather:
        temperature = main_data.get("temp")
        humidity = main_data.get("humidity")
        weather_description = weather.get("description")

        print(f"Weather in {name}, {country}:")
        print(f"Temperature: {temperature} degrees")
        print(f"Humidity: {humidity}")
        print(f"Conditions: {weather_description.capitalize()}")
    else:
        print("Incomplete weather data.")

def main():
    api_key = "b0a5b574ad87fd3468a1a087f13eb324"  # Replace with your desired OpenWeatherMap API key
    location = input("Enter a city or ZIP Code: ")
    data = fetch_weather_data(api_key, location)
    display_weather_data(data)

if __name__ == "__main__":
    main()
