from django.urls import path
from project.accounts.views import RegistrationView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register', RegistrationView.as_view(), name='register'),
]
