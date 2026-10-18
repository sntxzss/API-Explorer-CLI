import httpx

j_url = "https://official-joke-api.appspot.com/random_joke"

def get_joke():
    try:
        result = httpx.get(j_url, params={})
        result.raise_for_status()
        data = result.json()
        return (data['setup'], data['punchline'])
    except httpx.RequestError:
        return {"error": "No connection"}
    except httpx.HTTPStatusError:
        return {"error": "Server error"}