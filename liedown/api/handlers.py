from datetime import datetime
from flask import jsonify, current_app, request, g
from json import loads

from .exceptions import ApiException


def setup_handlers(app):

    @app.before_request
    def log_request_info():
        g.start = datetime.now()
        log_data = {'request-id': request.headers.get('Request-Id'),
                    'user-agent': request.headers.get('User-Agent'),
                    'url': request.url}

        log_data['data'] = request.json or {}

        current_app.logger.info('Request Data: {0}'.format(log_data))

    @app.after_request
    def log_response_info(response):
        time = datetime.now() - g.start

        log_data = {'url': request.url,
                    'response_code': response.status_code,
                    'time': '%s.%s' % (time.seconds, time.microseconds),
                    'data': loads(response.data)}

        request_id = response.headers.get('Request-Id')
        if request_id:
            log_data['request-id'] = request_id

        current_app.logger.info('Response Data: {0}'.format(log_data))
        return response

    @app.after_request
    def add_request_id_header(response):
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
