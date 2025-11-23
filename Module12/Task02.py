import requests

def main():
    api_key = "194d986453b761193c2e2e9bef5c0fa5"
    city = input("Enter the name of a municipality: ")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_description = data["weather"][0]["description"]
        temp_kelvin = data["main"]["temp"]
        temp_celsius = temp_kelvin - 273.15
        print(f"Weather in {city}: {weather_description}")
        print(f"Temperature: {temp_celsius:.2f}°C")
    else:
        print("Failed to fetch weather data. Check the city name or API key.")

main()
