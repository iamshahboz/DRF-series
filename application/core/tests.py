from django.test import TestCase
from core.models import User, Order
from django.urls import reverse 



class UserOrderTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='user1',password='test1')
        user2 = User.objects.create_user(username='user2',password='test2')
        Order.objects.create(user=user1)
        Order.objects.create(user=user1)
        Order.objects.create(user=user2)
        Order.objects.create(user=user2)

    def test_user_order_endpoint_retrieves_only_authenticated_user_orders(self):
        user = User.objects.get(username='user1')
        self.client.force_login(user)
        response = self.client.get(reverse('user-orders'))

        assert response.status_code == 200
        data = response.json()
        print(data)



