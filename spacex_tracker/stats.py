from typing import List, Dict
from collections import Counter
from datetime import datetime

def success_rate_by_rocket(launches: List[Dict]) -> Dict[str, float]:
    rockets = {}
    for launch in launches:
        rocket = launch["rocket"]
        rockets.setdefault(rocket, []).append(launch["success"])
    return {r: sum([s for s in results if s])/len(results) for r, results in rockets.items()}

def launches_by_site(launches: List[Dict]) -> Dict[str, int]:
    sites = [l.get("launchpad") for l in launches]
    return dict(Counter(sites))

def monthly_launch_frequency(launches: List[Dict]) -> Dict[str, int]:
    months = [datetime.fromisoformat(l["date_utc"]).strftime("%Y-%m") for l in launches]
    return dict(Counter(months))
