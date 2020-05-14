
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser


class AccountTests(APITestCase):
    def test_notification(self):

        # Create user

        url_register = "http://127.0.0.1:8000/api/user/register/"
        data = {'email': 'question@gmail.com', 'password': '123', 'confirm_password': '123'}
        response = self.client.post(url_register, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.get().email, 'question@gmail.com')

        # Login

        user = CustomUser.objects.get(email='question@gmail.com')
        user.is_active = True
        user.save()
        url_login = "http://127.0.0.1:8000/api/user/login/"
        data = {'email': 'question@gmail.com', 'password': '123'}
        response = self.client.post(url_login, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Authorization

        token = response.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        user.save()

        # Post Question

        url = "http://127.0.0.1:8000/api/question/"
        data = {'title': 'True', 'type': 'False'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get Question

        url = "http://127.0.0.1:8000/api/question/1"
        response = self.client.get(url, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
