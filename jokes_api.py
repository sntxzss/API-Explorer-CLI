import httpx
j_url = "https://official-joke-api.appspot.com/random_joke"
def get_joke():
    result = httpx.get(j_url, params={})
    data = result.json()
    return (data['setup'], data['punchline'])