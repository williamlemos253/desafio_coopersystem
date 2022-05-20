from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory, APIClient
from .models import Product
from .views import ProductsAPIView, OrderAPIView
from freezegun import freeze_time
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import force_authenticate

# Create your tests here.
class ProductsManagerAPIViewTestCase(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
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
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.user.save()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    def test_create_product(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        request = self.factory.post(self.api_url+'products/', {'name': 'teste', 'price': 10, 'qtd': 10})
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.product_view(request)
        print('ver aqui',response.data)
        self.assertEqual(response.data, {'name': 'teste', 'price': '10.00', 'qtd': 10, 'status': 'Disponível'})
    
    def test_get_products(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        post = self.factory.post(self.api_url+'products/', {'name': 'teste', 'price': 10, 'qtd': 10})
        force_authenticate(post, user=self.user, token=self.user.auth_token)
        self.product_view(post)
        request = self.factory.get(self.api_url+'products/', format='json')
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.product_view(request)
        self.assertEqual(response.data[0], {'name': 'teste', 'price': '10.00', 'qtd': 10, 'status': 'Disponível'})

    def test_get_products_by_name(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        post = self.factory.post(self.api_url+'products/', {'name': 'teste', 'price': 10, 'qtd': 10})
        force_authenticate(post, user=self.user, token=self.user.auth_token)
        self.product_view(post)
        request = self.factory.get(self.api_url+'product/teste',format="json")
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.product_view(request)
        self.assertEqual(response.data[0], {'name': 'teste', 'price': '10.00', 'qtd': 10, 'status': 'Disponível'})

    def test_get_products_with_status_unavailable(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        post = self.factory.post(self.api_url+'products/', {'name': 'teste', 'price': 10, 'qtd': 0})
        force_authenticate(post, user=self.user, token=self.user.auth_token)
        self.product_view(post)
        request = self.factory.get(self.api_url+'product/teste',format="json")
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.product_view(request)
        self.assertEqual(response.data[0]['status'], 'Indisponível')

    def test_get_products_by_name_not_found(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        request = self.factory.get(self.api_url+'product/teste',format="json")
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.product_view(request)
        self.assertEqual(response.data, [])

    @freeze_time("2022-05-20")
    def test_order(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        request = self.factory.post(self.api_url+'products/', {'name': 'teste', 'price': 10, 'qtd': 10})
        force_authenticate(request, user=self.user, token=self.user.auth_token)
        response = self.product_view(request)
        order_request = self.factory.post(self.api_url+'orders/', self.order_data)
        force_authenticate(order_request, user=self.user, token=self.user.auth_token)
        order_response = self.order_view(order_request)
        self.assertEqual(order_response.data, {'product': 1, 'qtd': 2, 'unit_price': '10.00', 'total_price': '20.00', 'request_date': '2022-05-20T00:00:00Z', 'requester': 'william', 'postal_code': '95555000', 'uf': 'rs', 'City': 'porto alegre', 'address': 'rua teste bairro teste perto do mercado teste', 'Forwarding_agent': 'Sr Testador', 'status': 'Pendente'})

