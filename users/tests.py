from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser

# Create your tests here.
class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = "http://127.0.0.1:8000/api/user/register"
        data = {'email': 'name@gmail.com','password':'123','confirm_password':'123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CustomUser.objects.get().email, 'name@gmail.com')
    def active_account(self):
        url = "http://127.0.0.1:8000/api/user/register"
        data = {'email': 'name@gmail.com', 'password': '123', 'confirm_password': '123'}
        response = self.client.post(url, data, format='json')
