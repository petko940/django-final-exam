from django.urls import path
from .views import HomeMotherboardView, CreateMotherboardView, DetailsMotherboardView, EditMotherboardView, \
    DeleteMotherboardView

urlpatterns = [
    path('', HomeMotherboardView.as_view(), name='home_motherboard'),
    path('create', CreateMotherboardView.as_view(), name='create_motherboard'),
    path('details/<int:pk>/', DetailsMotherboardView.as_view(), name='detail_motherboard'),
    path('edit/<int:pk>/', EditMotherboardView.as_view(), name='edit_motherboard'),
    path('delete/<int:pk>/', DeleteMotherboardView.as_view(), name='delete_motherboard'),
]
