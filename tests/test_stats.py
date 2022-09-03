""" Test Stats helper. """
import mongomock
from app.models.calc import Calc
from app.models.stats import Stats
from app.helpers.stats import get_stats


calc = Calc("test", "mongodb://localhost",
            client=mongomock.MongoClient)
	
stats = Stats("test", "mongodb://localhost",
              client=mongomock.MongoClient)


def test_get_stats():
    """ Test the get_stats method. """
    stats.increase_successful(1)
    assert get_stats(calc, stats, 0) is not None
