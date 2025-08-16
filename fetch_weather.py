import requests
import datetime

def fetch_weather_data(lat: float = 12.9716, lon: float = 77.5946, city: str = "Bengaluru"):
    """Fetch current weather from Open‑Meteo (no API key required).

    Returns a dict compatible with insert_to_db.insert_weather_to_db.
    """
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    cw = r.json()["current_weather"]
    return {
        "city": city,
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "temp_c": float(cw["temperature"]),
        "windspeed": float(cw["windspeed"]),
        "weathercode": int(cw["weathercode"]),
    }
