""" Test config file for the application. """

from app.config import app_config


def test_config():
    """ Test the config file. """

    assert app_config["db"]["uri"] == "mongodb://root:pass@0.0.0.0:27017"
    assert app_config["db"]["name"] == "kuriboh"
    assert app_config["app"]["host"] == "0.0.0.0"
    assert app_config["app"]["port"] == "5555"
    assert app_config["app"]["debug"] == "True"
