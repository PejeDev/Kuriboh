""" Test database factory """
import mongomock

from app.factory.database import Database

database = Database("test", "mongodb://localhost",
                    client=mongomock.MongoClient)

def test_client():
    """ Test the client property. """
    assert database.client is not None

def test_insert():
    """ Test the insert method. """
    database.insert({ "test": "test" }, "test")
    assert database.find_by_property("test", "test", "test") is not None

def test_find_first():
    """ Test the find_first method. """
    assert database.find_first("test") is not None

def test_update():
    """ Test the update method. """
    database.insert({ "test": "test" }, "test")
    found = database.find_by_property("test", "test", "test")
    assert database.update(found["_id"], {"test2": "test2"}, "test") is True

def test_delete():
    """ Test the delete method. """
    database.insert({ "test": "test" }, "test")
    found = database.find_by_property("test", "test", "test")
    assert database.delete(found["_id"], "test") is True
