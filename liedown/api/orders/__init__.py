from flask import Blueprint, request
from flask_restful import Resource

from ..base import Api
from ..exceptions import ApiException
from .schema import OrderSchema

# named Blueprint object, so as to be registered by the app factory
BLUEPRINT = Blueprint('orders', __name__, url_prefix='/orders')
api = Api(BLUEPRINT)


class Order(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)


@api.resource('/')
class OrdersResource(Resource):

    def post(self):
        """ Create an order """
        schema = OrderSchema()

        order_data, request_errors = schema.load(request.json)
        if request_errors:
            raise ApiException(request_errors)

        order = Order(**order_data)

        response, response_errors = schema.dump(order)
        if response_errors:
            return {
                'message': "Apologies, there's been an unexpected error."}, 500
        return response, 201
