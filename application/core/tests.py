from django.urls import reverse 
from core.models import User, Product 
from rest_framework.test import APITestCase

# Create tests here 

class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(username='admin',password='adminpass')
        self.normal_user = User.objects.create_user(username='user',password='userpass')
        self.product = Product.objects.create(
            name = "Test Product",
            description = "Test description",
            price = 9.99,
            stock = 10
        )
        #don't forget to put the name of your application in reverse
        self.url = reverse('core:product-detail', kwargs={'product_id': self.product.pk})

    def test_get_product(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['name'], self.product.name)

