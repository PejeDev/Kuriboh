""" Flask routes handler. """

from flask import jsonify


def configure_routes(app):
    """ Configures the routes for the application. """

    @app.route('/api/health', methods=['GET'])
    def get_health():
        """ Health check endpoint. """
        return jsonify({
            'status': 'ok'
        }), 200
