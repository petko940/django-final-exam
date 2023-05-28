from django.contrib.auth.views import LogoutView
from django.urls import path
from project.accounts.views import RegistrationView, HomeView, Logout, SignInView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('register', RegistrationView.as_view(), name='register'),
    path('login', SignInView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),

]
