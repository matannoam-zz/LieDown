from flask import jsonify, current_app, request

from .exceptions import ApiException


def setup_handlers(app):

    @app.before_request
    def check_authentication_token():
        authentication_token = request.headers.get('Authentication-Token')
        if authentication_token != 'SECRET':
            return jsonify({
                'message': 'Authentication token misssing or incorrect.'}), 403

    @app.after_request
    def add_request_id_header(response):
        # don't include request id on forbidden
        if response.status_code == 403:
            return response

        request_id = request.headers.get('Request-Id')
        if request_id:
            response.headers.extend({'Request-Id': request_id})
        return response

    @app.errorhandler(ApiException)
    def bad_request(e):
        return jsonify({'errors': e.errors}), 400

    @app.errorhandler(Exception)
    def internal_server_error(e):
        current_app.logger.exception(e)
        return jsonify({
            'message': "Apologies, there's been an unexpected error."}), 500
