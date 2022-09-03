""" Test Stats helper. """
from app.helpers.stats import calculate_stats

def test_calculate_stats():
    """ Test the calculate_statsmethod. """
    stats = {
        "successful": 1,
        "failed": 0,
        "total": 1
    }
    assert calculate_stats(100, stats) is not None
