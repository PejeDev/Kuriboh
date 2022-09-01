"""Flask Application"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/health', methods=['GET'])
def get_health():
    """ Health check endpoint. """
    return jsonify({
        'status': 'ok'
    }), 200
