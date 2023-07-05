from django.urls import path

from project.ram.views import HomeRamView, CreateRamView, RAMInformationView, EditRamView, DeleteRamView

urlpatterns = [
    path('', HomeRamView.as_view(), name='home_ram'),
    path('choose/', CreateRamView.as_view(), name='choose_ram'),
    path('details/<int:pk>/', RAMInformationView.as_view(), name='detail_ram'),
    path('edit/<int:pk>/', EditRamView.as_view(), name='edit_ram'),
    path('delete/<int:pk>/', DeleteRamView.as_view(), name='delete_ram'),
]
