from django.contrib.auth import get_user_model

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
        response = self.client.post(self.register_url, {
            'username': 'testuser',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })

        self.assertEqual(response.status_code, 302)

        self.assertEqual(response.url, reverse('home'))

        self.assertTrue(User.objects.filter(username='testuser').exists())

        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_registration_view_authenticated_user(self):
        User.objects.create_user(username='existinguser', password='password')
        self.client.login(username='existinguser', password='password')

        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 302)

        self.assertEqual(response.url, reverse('home'))

    def test_registration_view_unauthenticated_user(self):
        response = self.client.get(self.register_url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'accounts/register.html')

        self.assertIsInstance(response.context['form'], RegistrationForm)


class SignInViewTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

        self.url = reverse('login')

    def test_sign_in_view_authenticated_user_redirect(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.url)

        self.assertRedirects(response, reverse('home'))

    def test_sign_in_view_unauthenticated_user(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'accounts/login.html')


class ProfileViewTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_profile_view(self):
        url = reverse('profile', kwargs={'username': self.username})

        self.client.login(username=self.username, password=self.password)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'accounts/profile.html')

        self.assertIn('cpus', response.context)
        self.assertIn('gpus', response.context)
        self.assertIn('rams', response.context)
        self.assertIn('storages', response.context)
        self.assertIn('motherboards', response.context)


class DeleteProfileViewTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_delete_profile_view(self):
        url = reverse('profile_delete', kwargs={'username': self.username})

        self.client.login(username=self.username, password=self.password)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'accounts/delete.html')

        user_model = get_user_model()
        user_obj = user_model.objects.get(username=self.username)
        self.assertEqual(response.context['object'], user_obj)

        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('home'))

        with self.assertRaises(user_model.DoesNotExist):
            user_model.objects.get(username=self.username)


class ProfileUsernameChangeViewTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

        self.url = reverse('profile_username_change_view', kwargs={'username': self.username})

        self.client = Client()

    def test_profile_username_change_view_unauthenticated_user(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('login') + f'?next={self.url}')

    def test_profile_username_change_view_authenticated_user(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'accounts/change-username.html')


class ProfilePasswordChangeViewTest(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

        self.url = reverse('profile_change_password', kwargs={'username': self.username})

        self.client = Client()

    def test_profile_password_change_view_unauthenticated_user(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, reverse('login') + f'?next={self.url}')

    def test_profile_password_change_view_authenticated_user(self):
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'accounts/change-password.html')
