from django.urls import path
from project.accounts.views import RegistrationView

urlpatterns = [
    path('/register',RegistrationView.as_view())
]
