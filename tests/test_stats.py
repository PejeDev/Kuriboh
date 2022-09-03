""" Test Stats helper. """
from app.helpers.stats import calculate_stats

def test_calculate_stats():
    """ Test the calculate_statsmethod. """
    result_count = 50
    assert calculate_stats(result_count, 100) is not None
    assert calculate_stats(result_count, 100)["total"] == 100
    assert calculate_stats(result_count, 100)["count"] == result_count
    assert calculate_stats(result_count, 100)["ratio"] == 0.5
