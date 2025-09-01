**README for Weather Applications Repository**

---

# Weather Applications Collection

This repository contains **three different weather applications** demonstrating various technologies and approaches to fetch and display weather data using API keys.

---

## Applications Included

1. **Flask Weather App**  
   A web application built with the Flask framework (Python) that fetches weather data from an external API.

2. **Static HTML & CSS Weather App**  
   A simple weather app using plain HTML, CSS, and JavaScript to fetch weather data from an API.

3. **Python Weather Script**  
   A standalone Python script that fetches and displays weather information using an API.

---

## Getting Started

### Prerequisites

- You need a valid **weather API key** from a weather data provider (e.g., OpenWeatherMap, WeatherAPI, etc.).
- For the Flask app and Python script, Python 3.x should be installed.
- For the Flask app, it is recommended to use a virtual environment.

---

## Setup Instructions

### 1. Flask Weather App

- Navigate to the Flask app directory.
- Create a `.env` file or set environment variables to store your API key securely.

Example `.env` file:
```
WEATHER_API_KEY=your_api_key_here
```

- Install dependencies:
```bash
pip install -r requirements.txt
```

- Run the Flask app:
```bash
flask run
```

- The app will use the API key from the environment to fetch weather data.

---

### 2. Static HTML & CSS Weather App

- Open the HTML file in a web browser.
- Locate the JavaScript section where the API key is defined.
- Replace the placeholder API key with your own:

```js
const API_KEY = 'your_api_key_here';
```

- Save the file and refresh the browser to use your API key.

---

### 3. Python Weather Script

- Navigate to the Python script directory.
- Open the script file.
- Find the variable where the API key is set and replace it with your own:

```python
API_KEY = 'your_api_key_here'
```

- Run the script:

```bash
python weather_script.py
```

---

## Notes

- **Keep your API keys private!** Do not commit your API keys to public repositories.
- Use `.gitignore` to exclude `.env` files or any files containing sensitive information.
- You can obtain free API keys from popular weather services such as:
  - [OpenWeatherMap](https://openweathermap.org/api)
  - [WeatherAPI](https://www.weatherapi.com/)
  - [Weatherbit](https://www.weatherbit.io/api)

---
weather-apps/
│
├── flask-weather_Api
│   ├── app.py                  # Main Flask application
│   ├── requirements.txt        # Python dependencies
│   ├── .env                    # Environment variables (API key) - add to .gitignore
│   ├── templates/              # HTML templates (Jinja2)
│   │   └── index.html

|---Weather.html
│--Weather.py

---

## Contact

For questions or suggestions, please open an issue or contact the repository maintainer.

---

**Thank you for using these weather applications!**
