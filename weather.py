import requests

def get_weather(city, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    try:
        response = requests.get(f"{base_url}?key={api_key}&q={city}&aqi=no")
        response.raise_for_status()  # Raises an error for bad status codes
        weather_data = response.json()
        
        location = weather_data['location']
        current = weather_data['current']
        
        print("\n Weather Information ")
        print(f" {location['name']}, {location['country']}")
        print(f" Temperature: {current['temp_c']}°C (Feels like {current['feelslike_c']}°C)")
        print(f" Condition: {current['condition']['text']}")
        print(f" Humidity: {current['humidity']}%")
        print(f" Wind: {current['wind_kph']} km/h")
        print(f" Last updated: {current['last_updated']}")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

def main():
    print(" Simple Weather App ")
    api_key = "a08b1f30739842588b6130142251108"
    
    while True:
        city = input("\nEnter city name (or 'quit' to exit): ").strip()
        if city.lower() == 'quit':
            print("Goodbye! ")
            break
        
        if city:
            get_weather(city, api_key)
        else:
            print("Please enter a valid city name.")

if __name__ == "__main__":
    main()
