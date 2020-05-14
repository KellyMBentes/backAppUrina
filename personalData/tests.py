
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser


class AccountTests(APITestCase):
    def test_personal_data(self):

        # Create user

        url_register = "http://127.0.0.1:8000/api/user/register/"
        data = {'email': 'personal@gmail.com', 'password': '123', 'confirm_password': '123'}
        response = self.client.post(url_register, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.get().email, 'personal@gmail.com')

        # Login

        user = CustomUser.objects.get(email='personal@gmail.com')
        user.is_active = True
        user.save()
        url_login = "http://127.0.0.1:8000/api/user/login/"
        data = {'email': 'personal@gmail.com', 'password': '123'}
        response = self.client.post(url_login, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Authorization

        token = response.data.get('token')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        user.save()


        # Post Personal Data
        url = "http://127.0.0.1:8000/api/personal-data/"
        data = {'name': 'Teste', 'birthDate': '2020-02-02', 'gender': 'masculino', 'cpf': 'This fie', 'rg': 'This fi',
                'cep': 'This fie', 'addressNumber': 'This fie', 'addressStreet': 'This f.', 'addressCity': 'This fiel.',
                'addressDistrict': 'This fd.', 'addressFederalState': 'This fied.', 'healthEnsurance': True,
                'healthEnsuranceCompany': 'This fiequired.', 'healthEnsuranceDescription': 'This s reqed.',
                'hasHealthData': True, 'hasPrescription': True, 'hasQrMedication': True, 'schooling': 'This field is red.',
                'civilStatus': 'This fieired.', 'birthPlace': 'This fielquired.', 'occupation': 'This field iuired.',
                'ethnicity': 'This fiequired.', 'familyIncome': 'This firequired.'}
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get Personal Data

        url = "http://127.0.0.1:8000/api/personal-data/1"
        response = self.client.get(url, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Post Phone
        url = "http://127.0.0.1:8000/api/personal-data/1/phone/"
        data = {'number': '9999999999'}
        response = self.client.post(url, data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Get phone

        url = "http://127.0.0.1:8000/api/personal-data/phone/1"
        response = self.client.get(url, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
