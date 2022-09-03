""" Tests for the app routes. """
from unittest.mock import patch
from flask import Flask
from pytest_mock_resources import create_mongo_fixture

from app.server import app
from app.handlers.routes import configure_routes

database = create_mongo_fixture()

def test_route_configuration():
    """ Test the route configuration. """
    server = Flask(__name__)
    configure_routes(server)
    client = server.test_client()
    url = '/api/health'
    response = client.get(url)
    assert response.status_code == 200


def test_health_route():
    """ Test the api health route. """
    client = app.test_client()
    url = '/api/health'
    response = client.get(url)
    assert response.status_code == 200

@patch('app.models.calc.Calc.add')
def test_get_smallest_positive_interger_route(_):
    """ Test the get_smallest_positive_interger route. """
    client = app.test_client()
    url = '/api/smallest'
    response = client.post(url, json={'array': [-1, -3]})
    assert response.status_code == 200
    assert response.json['result'] == 1
    response = client.post(url, json={'list': [-1, -3]})
    assert response.status_code == 401
    assert response.json['error'] == "'array' is a required property"
    response = client.post(url, json={'array': ["-1", -3]})
    assert response.status_code == 401
    assert response.json['error'] == "'-1' is not of type 'integer'"
    response = client.post(url)
    assert response.status_code == 401
    assert response.json['error'] == "bad request"
