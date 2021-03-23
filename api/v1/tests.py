from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APITestCase
from api.v1.models import Contact

# Create your tests here.

class ContactTests(APITestCase):
    def test_create_contact(self):
        """
        Ensure we can create a new contact object.
        """
        url = 'http://localhost:8000/contacts/'
        data = {
            'name': 'test name',
            'email': 'test@example.com',
            'title': 'test title',
            'content': 'test content',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Contact.objects.count(), 1)
        self.assertEqual(Contact.objects.get().name, 'test name')
        self.assertEqual(Contact.objects.get().email, 'test@example.com')
        self.assertEqual(Contact.objects.get().title, 'test title')
        self.assertEqual(Contact.objects.get().content, 'test content')
