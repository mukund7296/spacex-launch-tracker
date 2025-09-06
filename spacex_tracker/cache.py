import json
from pathlib import Path
from typing import Any

CACHE_DIR = Path("./cache")
CACHE_DIR.mkdir(exist_ok=True)

def save_cache(filename: str, data: Any):
    with open(CACHE_DIR / filename, "w") as f:
        json.dump(data, f)

def load_cache(filename: str) -> Any:
    try:
        with open(CACHE_DIR / filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
