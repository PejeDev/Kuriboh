"""Flask Application"""
from flask import Flask
from app.handlers.routes import configure_routes

app = Flask(__name__)

configure_routes(app)
