from django.shortcuts import redirect
from django.urls import path
from project.accounts.views import RegistrationView, HomeView, Logout, SignInView, ProfileView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('register', RegistrationView.as_view(), name='register'),
    path('login', SignInView.as_view(), name='login'),
    path('logout', Logout.as_view(), name='logout'),

    path('register/', lambda request: redirect('/register'), name='register'),
    path('login/', lambda request: redirect('/login'), name='login'),

    # change
    path('profile', ProfileView.as_view(), name='profile'),
    # path('/profile/change-username', ProfileChangeUsernameView.as_view(), name='change_username'),
    # path('/profile/change-password', ProfileChangePasswordView.as_view(), name='change_password'),

]
