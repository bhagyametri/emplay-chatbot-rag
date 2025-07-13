import requests

def search_web_serper(query, api_key):
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "q": query
    }
    response = requests.post(url, headers=headers, json=payload)
    results = response.json().get("organic", [])
    return results[:3]  # top 3

