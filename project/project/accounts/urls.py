from django.urls import path, include, reverse_lazy
from project.accounts.views import RegistrationView, Logout, SignInView, ProfileView, DeleteProfileView, \
    ProfilePasswordChangeView, profile_username_change_view, access_denied_view

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),

    # without slag
    # path('profile/',include([
    #     path('', ProfileView.as_view(), name='profile_no_slug'),
    #     path('delete/', DeleteProfileView.as_view(), name='profile_delete'),
    #     path('change-username/', profile_username_change_view, name='profile_username_change_view'),
    #     path('change-password/', ProfilePasswordChangeView.as_view(), name='profile_change_password_no_slug'),
    # ])),

    path('access-denied/', access_denied_view, name='access_denied_view'),

    path('profile/<username>/', include([
        path('', ProfileView.as_view(), name='profile'),
        path('delete/', DeleteProfileView.as_view(), name='profile_delete'),
        path('change-username/', profile_username_change_view, name='profile_username_change_view'),
        path('change-password/', ProfilePasswordChangeView.as_view(), name='profile_change_password'),
    ])),

]
