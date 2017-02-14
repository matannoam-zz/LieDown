from unittest import TestCase
from mock import patch
from nose.tools import eq_

from liedown.api.orders import OrdersResource
from liedown.api.exceptions import ApiException


@patch('liedown.api.orders.request')
class OrdersTests(TestCase):

    def setUp(self):
        self.resource = OrdersResource()

    def test_post(self, mock_request):
        mock_request.json = {}

        response, status_code = self.resource.post()

        eq_(status_code, 201)
        eq_(response, {})

    def test_post_shipping_address_requires_zip_code(self, mock_request):
        mock_request.json = {'shipping_address': {}}

        with self.assertRaises(ApiException) as context:
            self.resource.post()

        eq_(context.exception.errors,
            {'shipping_address':
                {'zip_code': [u'Missing data for required field.']}})
