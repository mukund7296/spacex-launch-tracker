from datetime import datetime, timezone

def filter_launches(launches, rocket_id=None, start_date=None, end_date=None, success=None):
    filtered = launches

    # Parse start and end as UTC-aware datetimes
    if start_date:
        start = datetime.fromisoformat(start_date).replace(tzinfo=timezone.utc)
        filtered = [
            l for l in filtered
            if datetime.fromisoformat(l["date_utc"].replace("Z", "+00:00")) >= start
        ]

    if end_date:
        end = datetime.fromisoformat(end_date).replace(tzinfo=timezone.utc)
        filtered = [
            l for l in filtered
            if datetime.fromisoformat(l["date_utc"].replace("Z", "+00:00")) <= end
        ]

    if rocket_id:
        filtered = [l for l in filtered if l["rocket"] == rocket_id]

    if success is not None:
        filtered = [l for l in filtered if l["success"] is success]

    return filtered
