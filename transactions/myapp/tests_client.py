from django.test import TestCase
from django.urls import reverse
from .models import Transaction

class MoneyhubAPITestCase(TestCase):
    def setUp(self):
        # Set up test data, such as a client_id and secret_key
        self.client_id = '8d334bc5-ec8b-41a0-a864-fc8572e8b289'
        self.secret_key = 'f3442ad7-18e0-4d0c-804f-40f561bfd265'
        # Create a test transaction
        Transaction.objects.create(
            client_id=self.client_id,
            amount=100.0,
            description='Test client side Transaction',
        )

    def test_fetch_transactions(self):
        # Test fetching transactions using the test client_id and secret_key
        url = reverse('home')
        data = {'client_id': self.client_id, 'secret_key': self.secret_key}
        response = self.client.post(url, data, format='json')

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected content (e.g., transaction details)
        # You can adjust this based on the actual response format from the Moneyhub API
        self.assertIn('Test Transaction', response.content.decode())

    # Add more test cases as needed
