from spacex_tracker.launches import filter_launches

sample_launches = [
    {"date_utc": "2022-01-01T00:00:00.000Z", "rocket": "rocket1", "success": True, "launchpad": "pad1"},
    {"date_utc": "2023-01-01T00:00:00.000Z", "rocket": "rocket2", "success": False, "launchpad": "pad2"},
]

def test_filter_by_date():
    result = filter_launches(sample_launches, start_date="2022-12-31")
    assert len(result) == 1

def test_filter_by_rocket():
    result = filter_launches(sample_launches, rocket_id="rocket1")
    assert len(result) == 1
