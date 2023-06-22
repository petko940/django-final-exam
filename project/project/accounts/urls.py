from django.urls import path, include
from project.accounts.views import RegistrationView, Logout, SignInView, ProfileView, DeleteProfileView, \
    ProfileUsernameChangeView, ProfilePasswordChangeView

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    # change
    # path('profile', ProfileView.as_view(), name='profile'),
    path('profile/', include([
        path('', ProfileView.as_view(), name='profile'),
        path('delete/', DeleteProfileView.as_view(), name='profile_delete'),
        path('change-username/', ProfileUsernameChangeView.as_view(), name='profile_change_username'),
        path('change-password/', ProfilePasswordChangeView.as_view(), name='profile_change_password'),
    ]))
]
