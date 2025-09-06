import requests
from typing import List, Dict, Any
from .cache import load_cache, save_cache

BASE_URL = "https://api.spacexdata.com/v4"

def fetch_data(endpoint: str) -> List[Dict[str, Any]]:
    url = f"{BASE_URL}/{endpoint}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching {endpoint}: {e}")
        return []

def fetch_data_cached(endpoint: str) -> List[Dict[str, Any]]:
    cached = load_cache(f"{endpoint}.json")
    if cached:
        return cached
    data = fetch_data(endpoint)
    save_cache(f"{endpoint}.json", data)
    return data

