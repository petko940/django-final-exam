from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from project.accounts.forms import RegistrationForm


class RegistrationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')

    def test_registration_view_success(self):
        # Simulate a POST request to the registration view
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })

        # Check that the response has a 302 status code (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the user is redirected to the home page
        self.assertEqual(response.url, reverse('home'))

        # Check that a user with the specified username is created
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Check that the user is logged in
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_registration_view_authenticated_user(self):
        # Create an authenticated user
        User.objects.create_user(username='existinguser', password='password')
        self.client.login(username='existinguser', password='password')

        # Simulate a GET request to the registration view
        response = self.client.get(self.register_url)

        # Check that the response has a 302 status code (redirect)
        self.assertEqual(response.status_code, 302)

        # Check that the user is redirected to the home page
        self.assertEqual(response.url, reverse('home'))

    def test_registration_view_unauthenticated_user(self):
        # Simulate a GET request to the registration view
        response = self.client.get(self.register_url)

        # Check that the response has a 200 status code (success)
        self.assertEqual(response.status_code, 200)

        # Check that the template used is 'accounts/register.html'
        self.assertTemplateUsed(response, 'accounts/register.html')

        # Check that the context contains the registration form
        self.assertIsInstance(response.context['form'], RegistrationForm)
