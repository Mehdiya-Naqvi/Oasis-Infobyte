import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    if weather_data["cod"] != "404":
        main = weather_data["main"]
        # temperature = main["temp"]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_desc = weather_data["weather"][0]["description"]
        return f"Temperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {weather_desc}"
        # return f"Temperature: {temperature}°C"
    else:
        return "City not found"

def main():
    api_key = "98a8c04babeedc4b6d53b2dfc600f855"
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    print(weather_data)

if __name__ == "__main__":
    main()

