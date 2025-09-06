from spacex_tracker.stats import success_rate_by_rocket, launches_by_site, monthly_launch_frequency

sample_launches = [
    {"date_utc": "2022-01-01T00:00:00.000Z", "rocket": "rocket1", "success": True, "launchpad": "pad1"},
    {"date_utc": "2022-02-01T00:00:00.000Z", "rocket": "rocket1", "success": False, "launchpad": "pad1"},
    {"date_utc": "2022-03-01T00:00:00.000Z", "rocket": "rocket2", "success": True, "launchpad": "pad2"},
]

def test_success_rate_by_rocket():
    rates = success_rate_by_rocket(sample_launches)
    assert "rocket1" in rates
    assert isinstance(rates["rocket1"], float)

def test_launches_by_site():
    sites = launches_by_site(sample_launches)
    assert sites["pad1"] == 2

def test_monthly_launch_frequency():
    freq = monthly_launch_frequency(sample_launches)
    assert "2022-01" in freq
