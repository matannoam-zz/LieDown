from flask import Blueprint, request
from flask_restful import Api, Resource

from ..exceptions import ApiException
from .schema import OrderSchema
from .models import Order


# named Blueprint object, so as to be registered by the app factory
BLUEPRINT = Blueprint('orders', __name__, url_prefix='/orders')
api = Api(BLUEPRINT)


@api.resource('/')
class OrdersResource(Resource):

    def post(self):
        """ Create an order """
        schema = OrderSchema()

        order_data, request_errors = schema.load(request.json)
        if request_errors:
            raise ApiException(request_errors)

        order = Order(**(order_data or {}))

        response, response_errors = schema.dump(order)
        if response_errors:
            raise Exception(response_errors)
        return response, 201
