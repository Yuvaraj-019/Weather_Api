import requests
import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from datetime import datetime
import pytz

load_dotenv()
app = Flask(__name__,static_folder='static', template_folder='templates')

API_KEY = os.getenv("WEATHERAPI_KEY")  # WeatherAPI key
BASE_URL = "https://api.weatherapi.com/v1/forecast.json"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    forecast = None
    bg_class = "default-bg"
    time_of_day = None
    rain_type = None  # Changed to None initially
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        url = f"{BASE_URL}?key={API_KEY}&q={city}&days=5&aqi=yes&alerts=no"
        response = requests.get(url)
        data = response.json()
        print(data)  # Debug output

        if "error" in data:
            error = data["error"]["message"]
        else:
            condition_text = data["current"]["condition"]["text"].lower()
            temp_c = data["current"]["temp_c"]
            # Get local time from WeatherAPI response
            local_time_str = data["location"]["localtime"]  # Format: "YYYY-MM-DD HH:MM"
            local_time = datetime.strptime(local_time_str, "%Y-%m-%d %H:%M")
            local_hour = local_time.hour

            # Determine time of day
            if 6 <= local_hour < 12:
                time_of_day = "morning"
            elif 12 <= local_hour < 18:
                time_of_day = "afternoon"
            elif 18 <= local_hour < 21:
                time_of_day = "evening"
            else:  # 9 PM to 6 AM
                time_of_day = "night"

            # Enhanced rain type detection
            if any(x in condition_text for x in ["rain", "thunder", "storm", "drizzle"]):
                bg_class = "rain"
                if "thunder" in condition_text:
                    rain_type = "thunder"
                elif "light rain" in condition_text or "drizzle" in condition_text:
                    rain_type = "shower"
                else:
                    rain_type = "normal"  # Default rain type
            elif "snow" in condition_text:
                bg_class = "snow"
            elif "cloud" in condition_text:
                bg_class = "cloudy"
            elif "overcast" in condition_text:
                bg_class = "overcast"
            elif any(x in condition_text for x in ["mist", "fog", "haze"]):
                bg_class = "mist"
            elif "sunny" in condition_text or "clear" in condition_text:
                bg_class = "clear"
            else:
                bg_class = "default-bg"

            # Current weather details
            weather = {
                "city": data["location"]["name"],
                "country": data["location"]["country"],
                "temp": temp_c,
                "condition": data["current"]["condition"]["text"],
                "icon": "https:" + data["current"]["condition"]["icon"],
                "time_of_day": time_of_day.capitalize(),
                "local_time": local_time_str,
                "aqi": data["current"].get("air_quality", {}).get("us-epa-index", "N/A"),
                "uv": data["current"].get("uv", "N/A"),
                "pressure": data["current"].get("pressure_mb", "N/A"),
                "humidity": data["current"].get("humidity", "N/A"),
                "precip_chance": data["forecast"]["forecastday"][0]["day"].get("daily_chance_of_rain", "N/A")
            }

            # 5-day forecast
            forecast = [
                {
                    "date": day["date"],
                    "temp": day["day"]["avgtemp_c"],
                    "condition": day["day"]["condition"]["text"],
                    "icon": "https:" + day["day"]["condition"]["icon"]
                }
                for day in data["forecast"]["forecastday"][:5]
            ]

    return render_template("index.html", weather=weather, forecast=forecast,
                         bg_class=bg_class, time_of_day=time_of_day,
                         rain_type=rain_type, error=error)

if __name__ == "__main__":
    app.run(debug=True)
