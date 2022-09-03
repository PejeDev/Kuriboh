""" Validator factory module """
from datetime import datetime


class Validator():
    """ Validator factory class """
    def validate_type(self, element, desired_type):
        """ Validates type of element """
        if desired_type == "string":
            return isinstance(element, str)
        if desired_type == "datetime":
            return isinstance(element, datetime)
        if desired_type == "integer":
            return isinstance(element, int)
        if desired_type == "float":
            return isinstance(element, float)
        if desired_type == "boolean":
            return isinstance(element, bool)
        if desired_type == "list":
            return isinstance(element, list)
        raise ValueError("Invalid value for desired type")

    def validate_types(self, element, fields):
        """ Validates type of element """
        for field in fields:
            if field in element:
                if not self.validate_type(element[field], fields[field]):
                    return False
            return True

    def validate(self, element, fields, required_fields, optional_fields):
        """ Validates element """
        if not self.validate_types(element, fields):
            raise ValueError("Invalid type of field")

        element_fields  = set(element.keys())
        required_fields = set(required_fields)
        optional_fields = set(optional_fields)


        if len(required_fields - element_fields) > 0:
            raise ValueError("Required field missing")

        if len(element_fields - (required_fields | optional_fields)) > 0:
            print(element_fields)
            print(required_fields)
            print(optional_fields)
            print(len(element_fields - (required_fields | optional_fields)))
            raise ValueError("Invalid field in element")
