""" Test validator factory """

from app.factory.validator import Validator


def test_validate_type():
    """ Test the validate_type method. """
    validator = Validator()
    assert validator.validate_type("test", "string") is True
    assert validator.validate_type(1, "string") is False
    assert validator.validate_type(1, "integer") is True
    assert validator.validate_type(1.1, "integer") is False
    assert validator.validate_type(1.1, "float") is True
    assert validator.validate_type(1.1, "string") is False
    assert validator.validate_type(True, "boolean") is True
    assert validator.validate_type(True, "string") is False
    assert validator.validate_type(None, "string") is False
    assert validator.validate_type(None, "integer") is False
    assert validator.validate_type(None, "boolean") is False
    assert validator.validate_type(None, "float") is False
    assert validator.validate_type(None, "list") is False
    assert validator.validate_type([], "list") is True
    assert validator.validate_type([], "string") is False
    assert validator.validate_type([], "boolean") is False
    assert validator.validate_type([], "integer") is False
    assert validator.validate_type([], "float") is False
    assert validator.validate_type({}, "string") is False
    assert validator.validate_type({}, "boolean") is False
    assert validator.validate_type({}, "integer") is False


def test_validate_types():
    """ Test the validate_types method. """
    validator = Validator()
    assert validator.validate_types(
        {"test": "test"}, {"test": "string"}) is True
    assert validator.validate_types({"test": 1}, {"test": "string"}) is False
    assert validator.validate_types(
        {"test": 1}, {"test": "integer"}) is True
    assert validator.validate_types(
        {"test": 1.1}, {"test": "integer"}) is False
    assert validator.validate_types(
        {"test": 1.1}, {"test": "float"}) is True
    assert validator.validate_types(
        {"test": 1.1}, {"test": "string"}) is False
    assert validator.validate_types(
        {"test": True}, {"test": "boolean"}) is True
    assert validator.validate_types(
        {"test": True}, {"test": "string"}) is False
    assert validator.validate_types(
        {"test": None}, {"test": "string"}) is False
    assert validator.validate_types(
        {"test": None}, {"test": "integer"}) is False
    assert validator.validate_types(
        {"test": None}, {"test": "boolean"}) is False
    assert validator.validate_types(
        {"test": None}, {"test": "float"}) is False
    assert validator.validate_types(
        {"test": None}, {"test": "list"}) is False
    assert validator.validate_types({"test": []}, {"test": "list"}) is True
    assert validator.validate_types(
        {"test": []}, {"test": "string"}) is False
    assert validator.validate_types(
        {"test": []}, {"test": "boolean"}) is False
    assert validator.validate_types(
        {"test": []}, {"test": "integer"}) is False
    assert validator.validate_types(
        {"test": []}, {"test": "float"}) is False
