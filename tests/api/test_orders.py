from unittest import TestCase
from mock import patch
from nose.tools import eq_

from liedown.api.orders import OrdersResource


@patch('liedown.api.orders.request')
class OrdersTests(TestCase):

    def setUp(self):
        self.resource = OrdersResource()

    def test_post(self, mock_request):
        mock_request.json = {}

        response, status_code = self.resource.post()

        eq_(response, {})
        eq_(status_code, 201)
