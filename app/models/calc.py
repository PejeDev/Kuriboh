""" Calc model """
from pymongo import MongoClient
from app.factory.database import Database
from app.factory.validator import Validator


class Calc():
    """ Calc class model """

    def __init__(self, uri, db_name, client= MongoClient):
        """ Constructor """
        self.validator = Validator()
        self.database = Database(uri, db_name, client)

        self.collection_name = "calcs"

        self.fields = {
            "array": "list",
            "result": "integer",
            "hash": "string",
            "created": "datetime"
        }

        self.create_required_fields = ["array", "result", "hash"]
        self.create_optional_fields = []

    def add(self, calc):
        """ Create a calc """
        self.validator.validate(calc,
                                self.fields,
                                self.create_required_fields,
                                self.create_optional_fields)
        found = self.find_by_hash(calc["hash"])
        if not found:
            self.database.insert(calc, self.collection_name)

    def find_by_hash(self, item_hash):
        """ Find a calc by hash """
        return self.database.find_by_property("hash", item_hash, self.collection_name)

    def delete(self, item_id):
        """ Delete a calc """
        return self.database.delete(item_id, self.collection_name)

    def get_calcs_count(self):
        """ Get the number of calcs """
        return self.database.count(self.collection_name)
