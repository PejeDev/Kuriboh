""" Test Stats model """
import mongomock

from app.models.stats import Stats

stats_model = Stats("test", "mongodb://localhost",
                    client=mongomock.MongoClient)


def test_increase_successful():
    """ Test the increase_successful method. """
    stats_model.increase_successful(1)
    found = stats_model.database.find_first("Stats")
    assert found["successful"] == 1


def test_increase_failed():
    """ Test the increase_failed method. """
    stats_model.increase_failed(1)
    found = stats_model.database.find_first("Stats")
    assert found["failed"] == 1


def test_delete_stats():
    """ Test the delete method. """
    found = stats_model.database.find_first("Stats")
    assert stats_model.delete(found["_id"]) is True
