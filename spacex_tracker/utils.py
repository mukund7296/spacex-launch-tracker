from typing import Dict, Any

def summarize_launch(launch: Dict[str, Any]) -> str:
    """Return a short summary string of a launch."""
    name = launch.get("name", "Unknown")
    date = launch.get("date_utc", "N/A")
    success = launch.get("success", None)
    outcome = "Success ✅" if success else "Failure ❌" if success is False else "Unknown"
    return f"{date[:10]} | {name} | {outcome}"
