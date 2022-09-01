""" Runs the application. """
from app.server import app
from app.config import app_config

if __name__ == "__main__":
    app.run(debug=app_config["app"]["debug"] == "True",
            port=int(app_config["app"]["port"]), host=app_config["app"]["host"])
