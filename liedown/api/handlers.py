from flask import jsonify, current_app

from .exceptions import ApiException


def setup_handlers(app):

    @app.errorhandler(ApiException)
    def bad_request(e):
        current_app.logger.exception(e)
        return jsonify({'errors': e.errors}), 400

    @app.errorhandler(Exception)
    def internal_server_error(e):
        current_app.logger.exception(e)
        return jsonify({
            'message': "Apologies, there's been an unexpected error."}), 500
