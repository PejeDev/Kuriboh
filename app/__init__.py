"""Flask Application"""
from flask import Flask, jsonify
from app.config import config


def init():
    """Initialize the application"""
    app = Flask(__name__)

    @app.route('/api/health', methods=['GET'])
    def get_health():
        return jsonify({
            'status': 'ok'
        }), 200

    app.run(debug=config["app"]["debug"] == "True",
            port=int(config["app"]["port"]), host=config["app"]["host"])
