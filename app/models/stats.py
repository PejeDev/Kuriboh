""" Stats model """
from pymongo import MongoClient
from app.factory.database import Database
from app.factory.validator import Validator

class Stats():
    """ stat class model """
    # pylint: disable=too-many-instance-attributes

    def __init__(self, uri, db_name, client= MongoClient):
        self.validator = Validator()
        self.database = Database(uri, db_name, client)
        self.collection_name = "stats"

        self.fields = {
            "total": "integer",
            "successful": "integer",
            "failed": "integer",
            "updated": "datetime",
            "created": "datetime",
        }

        self.create_required_fields = ["total", "successful", "failed"]
        self.create_optional_fields = []

        self.update_required_fields = ["total"]
        self.update_optional_fields = ["successful", "failed", "_id", "created", "updated"]

    def increase_successful(self, amount):
        """ Increase successful by amount """
        found = self.database.find_first(self.collection_name)
        if found:
            found["total"] += amount
            found["successful"] += amount
            self._update(found["_id"], found)
        else :
            self._add({"total": amount, "successful": amount, "failed": 0})

    def increase_failed(self, amount):
        """ Increase failed by amount """
        found = self.database.find_first(self.collection_name)
        if found:
            found["total"] += amount
            found["failed"] += amount
            self._update(found["_id"], found)
        else :
            self._add({"total": amount, "successful": 0, "failed": amount})

    def get_stats(self):
        """ Get stats """
        stats = self.database.find_first(self.collection_name)
        if not stats:
            return {"total": 0, "successful": 0, "failed": 0}
        del stats["_id"]
        return stats

    def _add(self, stats):
        """ Add a stat """
        self.validator.validate(stats,
                                self.fields,
                                self.create_required_fields,
                                self.create_optional_fields)
        self.database.insert(stats, self.collection_name)

    def _update(self, item_id, stats):
        """ Update a stat """
        self.validator.validate(stats,
                                self.fields,
                                self.update_required_fields,
                                self.update_optional_fields)
        return self.database.update(item_id, stats, self.collection_name)

    def delete(self, item_id):
        """ Delete a stat """
        return self.database.delete(item_id, self.collection_name)
