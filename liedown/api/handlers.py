from flask import jsonify, current_app, request

from .exceptions import ApiException


def setup_handlers(app):

    @app.after_request
    def add_request_id_header(response):
        request_id = request.headers.get('Request-Id')
        if request_id:
            response.headers.extend({'Request-Id': request_id})
        return response

    @app.errorhandler(ApiException)
    def bad_request(e):
        current_app.logger.exception(e)
        return jsonify({'errors': e.errors}), 400

    @app.errorhandler(Exception)
    def internal_server_error(e):
        current_app.logger.exception(e)
        return jsonify({
            'message': "Apologies, there's been an unexpected error."}), 500
