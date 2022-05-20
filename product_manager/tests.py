from urllib import response
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .models import Product
from .views import ProductsAPIView, OrderAPIView
from freezegun import freeze_time

# Create your tests here.
class ProductsManagerAPIViewTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.product = Product.objects.all()
        self.api_url = 'api/v1/'
        self.product_view = ProductsAPIView.as_view()
        self.order_view = OrderAPIView.as_view()
        self.order_data = {
                            "product": 1,
                            "qtd": 2,
                            "request_date": "2022-05-20T00:00:00Z",
                            "requester": "william",
                            "postal_code": "95555000",
                            "uf": "rs",
                            "City": "porto alegre",
                            "address": "rua teste bairro teste perto do mercado teste",
                            "Forwarding_agent": "Sr Testador",
                            "status": "Pendente"
                            }

    def test_create_product(self):
        request = self.factory.post(self.api_url+'products/', {'name': 'teste', 'price': 10, 'qtd': 10})
        response = self.product_view(request)
        self.assertEqual(response.data, {'name': 'teste', 'price': '10.00', 'qtd': 10, 'status': 'Disponível'})

    def test_get_products(self):
        post = self.factory.post(self.api_url+'products/', {'name': 'teste', 'price': 10, 'qtd': 10})
        self.product_view(post)
        request = self.factory.get(self.api_url+'products/', format='json')
        response = self.product_view(request)
        self.assertEqual(response.data[0], {'name': 'teste', 'price': '10.00', 'qtd': 10, 'status': 'Disponível'})

    def test_get_products_by_name(self):
        post = self.factory.post(self.api_url+'products/', {'name': 'teste', 'price': 10, 'qtd': 10})
        self.product_view(post)
        request = self.factory.get(self.api_url+'product/teste',format="json")
        response = self.product_view(request)
        self.assertEqual(response.data[0], {'name': 'teste', 'price': '10.00', 'qtd': 10, 'status': 'Disponível'})

    def test_get_products_with_status_unavailable(self):
        post = self.factory.post(self.api_url+'products/', {'name': 'teste', 'price': 10, 'qtd': 0})
        self.product_view(post)
        request = self.factory.get(self.api_url+'product/teste',format="json")
        response = self.product_view(request)
        self.assertEqual(response.data[0]['status'], 'Indisponível')

    def test_get_products_by_name_not_found(self):
        request = self.factory.get(self.api_url+'product/teste',format="json")
        response = self.product_view(request)
        self.assertEqual(response.data, [])

    @freeze_time("2022-05-20")
    def test_order(self):
        request = self.factory.post(self.api_url+'products/', {'name': 'teste', 'price': 10, 'qtd': 10})
        response = self.product_view(request)
        order_request = self.factory.post(self.api_url+'orders/', self.order_data)
        order_response = self.order_view(order_request)
        self.assertEqual(order_response.data, {'product': 1, 'qtd': 2, 'unit_price': '10.00', 'total_price': '20.00', 'request_date': '2022-05-20T00:00:00Z', 'requester': 'william', 'postal_code': '95555000', 'uf': 'rs', 'City': 'porto alegre', 'address': 'rua teste bairro teste perto do mercado teste', 'Forwarding_agent': 'Sr Testador', 'status': 'Pendente'})
        

