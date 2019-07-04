from django.test import TestCase, RequestFactory

from .views import index


# Create your tests here.
class OrdersViewTest(TestCase):
    fixtures = ['items.yaml', 'orders.yaml']

    def setUp(self):
        self.request_factory = RequestFactory()

    def test_get_orders_returns_200(self):
        req = self.request_factory.get('/order/')
        res = index(req)

        self.assertEqual(res.status_code, 200)

    def test_get_orders_without_orderid_returns_search_message(self):
        req = self.request_factory.get('/order')
        res = index(req)
        message = res.context_data['message']

        self.assertEqual(message, 'Please search for an order')

    def test_get_orders_with_invalid_orderid_returns_notfound_message(self):
        req = self.request_factory.get('/order?order_id=1')
        res = index(req)
        message = res.context_data['message']

        self.assertEqual(message, 'Order does not exist')

    def test_get_orders_with_valid_orderid_returns_order(self):
        req = self.request_factory.get('/order?order_id=34992')
        res = index(req)
        order = res.context_data['order_details']

        self.assertEqual(order.customer_name, 'Jane Smith')
        self.assertEqual(order.id, 34992)
        line_items = res.context_data['line_items']

        self.assertEqual(line_items[0]['item__name'], 'Cloak')
        self.assertEqual(float(line_items[0]['total']), 49.98)
        vat_breakdown = res.context_data['vat_breakdown']

        self.assertEqual(vat_breakdown['net'], 96.72)
        self.assertEqual(vat_breakdown['vat'], 19.34)
        self.assertEqual(vat_breakdown['total'], 116.06)
