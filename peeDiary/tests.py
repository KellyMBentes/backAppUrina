
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser


class AccountTests(APITestCase):
    def test_pee_diary(self):

        # Create user

        url_register = "http://127.0.0.1:8000/api/user/register/"
        data = {'email': 'pee@gmail.com', 'password': '123', 'confirm_password': '123'}
        response = self.client.post(url_register, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.get().email, 'pee@gmail.com')

        # Login

        user = CustomUser.objects.get(email='pee@gmail.com')
        user.is_active = True
        user.save()
        url_login = "http://127.0.0.1:8000/api/user/login/"
        data = {'email': 'pee@gmail.com', 'password': '123'}
        response = self.client.post(url_login, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Authorization

        token = response.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        user.save()

        # Post PeeDiary

        url = "http://127.0.0.1:8000/api/pee-diary/"
        data = {'peeVolume': 100, 'effortToUrinate': 110,
                'hasLost': True, 'isDoingPhysicalActivity': True, 'referenceVolume': 200}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get PeeDiary

        url = "http://127.0.0.1:8000/api/pee-diary/1"
        response = self.client.get(url, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


"""
        # Get offset PeeDiary
        url = "http://127.0.0.1:8000/api/pee-diary?limit=1"
        response = self.client.get(url, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        """