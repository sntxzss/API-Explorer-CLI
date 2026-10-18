import httpx

geo_url = "https://geocoding-api.open-meteo.com/v1/search"
w_url = "https://api.open-meteo.com/v1/forecast"

def get_forecast(city: str):
    geo_responce = httpx.get(geo_url, params={"name": city})
    geo_data = geo_responce.json()

    if not geo_data.get("results"):
     return {"error": "city not found"}
