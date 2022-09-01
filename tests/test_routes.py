""" Tests for the app routes. """
from flask import Flask
from app.server import app
from app.handlers.routes import configure_routes


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
