from flask import request
from flask_restful import Api as _Api
from flask_restful.representations.json import output_json


class Api(_Api):

    def __init__(self, *args, **kwargs):

        super(Api, self).__init__(*args, **kwargs)

        @self.representation('application/json')
        def json_include_request_id(*args, **kwargs):
            request_id = request.headers.get('Request-Id')

            response = output_json(*args, **kwargs)

            if request_id:
                response.headers.extend({'Request-Id': request_id})

            return response
