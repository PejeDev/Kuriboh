""" Configuration file for the application. """
import os

app_config = {
    "db": {
        "uri": os.getenv('DATABASE_URI', "mongodb://root:pass@0.0.0.0:27017"),
        "name": os.getenv('DATABASE_NAME', 'kuriboh'),
    },
    "app": {
        "host": os.getenv('APP_HOST', '0.0.0.0'),
        "port": os.getenv("PORT", "5555"),
        "debug": os.getenv("DEBUG", "True"),
    }
}
