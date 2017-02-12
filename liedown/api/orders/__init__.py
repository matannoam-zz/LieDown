from flask import Blueprint, request
from flask_restful import Api, Resource

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
        request_schema = OrderSchema()
        order_data, request_errors = request_schema.load(request.json)
        order = Order(**order_data)

        response_schema = OrderSchema()
        response, response_errors = response_schema.dump(order)
        return response, 201
