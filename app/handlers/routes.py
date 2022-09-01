""" Flask routes handler. """
from flask import jsonify, request, make_response
from flask_expects_json import expects_json
from jsonschema import ValidationError
from app.helpers.calc import get_smallest_positive_integer_not_in_list


def configure_routes(app):
    """ Configures the routes for the application. """

    schema = {
        'type': 'object',
        'properties': {
            'array': {
                'type': 'array',
                'items': {
                    'type': 'integer'
                }
            }
        },
        'required': ['array']
    }

    @app.route('/api/health', methods=['GET'])
    def get_health():
        """ Health check endpoint. """
        return jsonify({
            'status': 'ok'
        }), 200

    @app.route('/api/smallest', methods=['POST'])
    @expects_json(schema)
    def get_smallest_positive_interger():
        """ Smallest positive integer not in list endpoint. """
        data = request.get_json()
        return jsonify({
            'result': get_smallest_positive_integer_not_in_list(data['array'])
        }), 200

    @app.errorhandler(400)
    def bad_request(error):
        """ Bad request error handler. """
        if isinstance(error.description, ValidationError):
            original_error = error.description
            return make_response(jsonify({'error': original_error.message}), 401)
        return make_response(jsonify({'error': "bad request"}), 401)
