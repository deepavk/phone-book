import base64
# Create your tests here.
# Add unit tests and Integration tests for each functionality.
from django.contrib.auth.models import User
from django.urls import reverse
from pip._vendor.requests.auth import HTTPBasicAuth
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from .serializers import ContactSerializer
from .models import Contact


class ContactTests(APITestCase):
    def setUp(self):
        self.data = {
            "name": "test",
            "email": "test@gmail.com",
            "address": "abcde",
            "phone_number": "8726354617"
        }
        self.client = APIClient()
        self.user = User.objects.create_user(username='test',
                                             email='test@test.com',
                                             password='test')
        self.contact = Contact.objects.create(**{
            "name": "test1",
            "email": "test1@gmail.com",
            "address": "abcdefg",
            "phone_number": "123456789"
        })
        self.client.force_authenticate(user=self.user)
        self.INVALID_ID = 0

    def test_create_contact(self):
        response = self.client.post('/api/contacts/', self.data,
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_contact(self):
        response = self.client.get('/api/contacts/1/', format='json')
        serializer = ContactSerializer(self.contact)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

        # test invalid get
        invalid_url = '/api/contacts/{}/'.format(self.INVALID_ID)
        response = self.client.get(invalid_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_contact(self):
        new_name = "new name"
        self.data['name'] = new_name
        response = self.client.patch('/api/contacts/1/', self.data,
                                     format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], new_name)

        # test invalid update
        invalid_url = '/api/contacts/{}/'.format(self.INVALID_ID)
        response = self.client.patch(invalid_url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_contact(self):
        response = self.client.delete('/api/contacts/1/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # test invalid delete
        invalid_url = '/api/contacts/{}/'.format(self.INVALID_ID)
        response = self.client.delete(invalid_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
