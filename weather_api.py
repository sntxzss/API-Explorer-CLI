import httpx

geo_url = "https://geocoding-api.open-meteo.com/v1/search"
w_url = "https://api.open-meteo.com/v1/forecast"

def get_forecast(city: str):
 try:
    geo_responce = httpx.get(geo_url, params={"name": city})
    geo_data = geo_responce.json()

    if not geo_data.get("results"):
     print("No such a city")
     return None

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_re = httpx.get(w_url, params={"latitude": lat, "longitude": lon, "current": "temperature_2m,wind_speed_10m"})
    weather_re.raise_for_status()
    weather_data = weather_re.json()
    return weather_data["current"]

 except httpx.RequestError:
    return {"error": "No connection"}
 except httpx.HTTPStatusError:
    return {"error": "Server error"}