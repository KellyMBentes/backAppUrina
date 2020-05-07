from django.contrib.auth.models import User
from rest_framework.test import force_authenticate

from django.test import TestCase
from rest_framework import status

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from users.models import CustomUser
from rest_framework.test import force_authenticate

# Include an appropriate Authorization: header on all requests.
#token = Token.objects.get(user__email='a@a.com')
#user = CustomUser.objects.get(id=1)
#print(user)
#token = Token.objects.get(user=user)
#print(token)
#client = APIClient()
#client.credentials(HTTP_AUTHORIZATION='Token ' + token.key),
#factory = APIRequestFactory()
#request = factory.post('/api/peeDiary/create', {'user': 1, 'createdDate': '2020-04-23T13:36:03.049+00:00', 'peeVolume': 100, 'effortToUrinate': 110, 'hasLost': True, 'isDoingPhysicalActivity': True, 'referenceVolume': 200}, format='json')



user = CustomUser.objects.create_user(email="breno_alves@msn.com", password="290199br")
token = Token.objects.get(user=user)
client = APIClient()
client.force_authenticate(user=user)
client.login(email=user.email, password=user.password)
print(user, token, token.key)

class AccountTests(APITestCase):
    def test_create_account(self):
        print(user, token, token.key)
        self.client = APIClient()
        url = "http://127.0.0.1:8000/api/peeDiary/create"
        data = {'createdDate': '2020-04-23T13:36:03.049+00:00', 'peeVolume': '100', 'effortToUrinate': '110', 'hasLost': True, 'isDoingPhysicalActivity': True, 'referenceVolume': '200'}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.post(url, data, format='json')
        print(response, url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)