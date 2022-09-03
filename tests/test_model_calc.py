""" Test calc model """
import mongomock

from app.models.calc import Calc

database = Calc("test", "mongodb://localhost",
                client=mongomock.MongoClient)

def test_get_calcs_count():
    """ Test the get_calcs_count method. """
    assert database.get_calcs_count() == 0
    database.add({"array": [-1, 2],
                  "result": 1,
                  "hash": hash(str([-1, 2]))
                  })
    assert database.get_calcs_count() == 1

def test_add():
    """ Test the add method. """
    item_hash = hash(str([1, 2, 3, 4, 5]))
    database.add({"array": [1, 2, 3, 4, 5],
                  "result": 6,
                  "hash": item_hash
                  })
    assert database.find_by_hash(item_hash) is not None


def test_find_by_hash():
    """ Test the find_by_hash method. """
    item_hash = hash(str([1, 2, 3]))
    database.add({"array": [1, 2, 3],
                  "result": 4,
                  "hash": item_hash
                  })
    assert database.find_by_hash(item_hash) is not None

def test_delete():
    """ Test the delete method. """
    item_hash = hash(str([1, 2]))
    database.add({"array": [1, 2],
                  "result": 3,
                  "hash": item_hash
                  })
    found = database.find_by_hash(item_hash)
    database.delete(found["_id"])
    assert database.find_by_hash(item_hash) is False
