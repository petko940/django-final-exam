from django.urls import path

from project.common.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
