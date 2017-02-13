from datetime import datetime
from flask import current_app, request, g
from json import loads


def setup_logging(app):

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
                    'time': time.seconds + time.microseconds / 10. ** 6,
                    'data': loads(response.data)}

        request_id = response.headers.get('Request-Id')
        if request_id:
            log_data['request-id'] = request_id

        current_app.logger.info('Response Data: {0}'.format(log_data))
        return response
