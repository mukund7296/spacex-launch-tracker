from spacex_tracker.api import fetch_data
from spacex_tracker.launches import filter_launches
from spacex_tracker.stats import success_rate_by_rocket, launches_by_site, monthly_launch_frequency
from tabulate import tabulate  # pip install tabulate

def main():
    # Fetch data from API
    launches = fetch_data("launches")
    rockets_data = fetch_data("rockets")
    sites_data = fetch_data("launchpads")

    # Map IDs to human-readable names
    rockets = {r['id']: r['name'] for r in rockets_data}
    sites = {s['id']: s['name'] for s in sites_data}

    # Example: Filter successful Falcon 1 launches
    falcon1_id = next((r['id'] for r in rockets_data if r['name'] == "Falcon 1"), None)
    if falcon1_id:
        filtered = filter_launches(launches, rocket_id=falcon1_id, success=True)
        print(f"Successful Falcon 1 launches: {len(filtered)}\n")

    # Success rate by rocket
    print("Success rate by rocket:")
    rates = success_rate_by_rocket(launches)
    table = [[rockets.get(rid, rid), f"{rate:.0%}"] for rid, rate in rates.items()]
    print(tabulate(table, headers=["Rocket", "Success Rate"], tablefmt="grid"))
    print()

    # Launches by site
    print("Launches by site:")
    site_counts = launches_by_site(launches)
    table = [[sites.get(sid, sid), count] for sid, count in site_counts.items()]
    print(tabulate(table, headers=["Launch Site", "Launches"], tablefmt="grid"))
    print()

    # Monthly launch frequency
    print("Monthly launch frequency:")
    monthly = monthly_launch_frequency(launches)
    table = [[month, count] for month, count in sorted(monthly.items())]
    print(tabulate(table, headers=["Month", "Launches"], tablefmt="grid"))

if __name__ == "__main__":
    main()
