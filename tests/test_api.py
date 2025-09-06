import pytest
from spacex_tracker.api import fetch_data

def test_fetch_launches():
    data = fetch_data("launches")
    assert isinstance(data, list)
    assert "name" in data[0]
