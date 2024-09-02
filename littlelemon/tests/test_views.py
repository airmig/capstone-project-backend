from django.test import TestCase
from django.urls import reverse
from restaurant.serializers import MenuSerializer
from restaurant.models import Menu
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='flerkin', password='cat@123!')
        
        # Generate a token for the test user
        self.token = Token.objects.create(user=self.user)
        
        # Create a client and authenticate with the token
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        
        self.menu1 = Menu.objects.create(title="Ice Cream", price=80.00, inventory=10)
        self.menu2 = Menu.objects.create(title="Pizza", price=150.00, inventory=20)
        self.menu3 = Menu.objects.create(title="Pasta", price=100.00, inventory=30)

    def test_getall(self):
        # Make a GET request to retrieve all Menu objects
        response = self.client.get(reverse('menu'))  # Assuming the URL name is 'menu-list'
        
        # Serialize the Menu objects
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Assert the response status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Assert the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)