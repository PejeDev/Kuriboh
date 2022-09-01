""" Configuration file for the application. """
import os

config = {
    "db": {
        "host": os.getenv('DATABASE_HOST', '0.0.0.0'),
        "port": os.getenv('DATABASE_PORT', '27017'),
        "name": os.getenv('DATABASE_NAME', 'kuriboh'),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD", "pass")
    },
    "app": {
        "host": os.getenv('APP_HOST', '0.0.0.0'),
        "port": os.getenv("PORT", "5555"),
        "debug": os.getenv("DEBUG", "True"),
    }
}
