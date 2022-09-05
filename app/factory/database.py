""" Database factory """
from datetime import datetime
from pymongo import MongoClient
from bson import ObjectId


class Database:
    """ Database module """

    def __init__(self, uri, db_name, client=MongoClient):
        """ Constructor """
        self.client = client(uri)
        self.database = self.client[db_name]

    def insert(self, element, collection_name):
        """ Insert element into collection """
        element["created"] = datetime.now()
        element["updated"] = datetime.now()
        inserted = self.database[collection_name].insert_one(
            element)
        return str(inserted.inserted_id)

    def find_all(self, collection_name):
        """ Find all elements from collection """
        found = self.database[collection_name].find(
            filter=None, projection=None, limit=0, sort=False)
        return list(found)

    def count_by_param(self, collection_name, param, param_value):
        """ Count elements in collection """
        criteria = { param: param_value }
        return self.database[collection_name].count_documents(criteria)

    def count_total(self, collection_name):
        """ Count elements in collection """
        return self.database[collection_name].count_documents({})

    def find_by_property(self, prop, prop_value, collection_name):
        """ Find element by id """
        found = self.database[collection_name].find_one({prop: prop_value})
        if found is None:
            return False

        if "_id" in found:
            found["_id"] = str(found["_id"])

        return found

    def find_first(self, collection_name):
        """ Find first element from collection """
        found = self.database[collection_name].find_one(
            filter=None, projection=None, limit=1, sort=False)
        return found

    def update(self, item_id, element, collection_name):
        """ Update element by id """
        criteria = {"_id": ObjectId(item_id)}

        element["updated"] = datetime.now()
        set_obj = {"$set": element}

        updated = self.database[collection_name].update_one(criteria, set_obj)
        return updated.matched_count == 1

    def delete(self, item_id, collection_name):
        """ Delete element by id """
        deleted = self.database[collection_name].delete_one(
            {"_id": ObjectId(item_id)})
        return bool(deleted.deleted_count)
