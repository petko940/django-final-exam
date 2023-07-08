from django.urls import path
from .views import HomeStorageView, ChooseStorageView, DetailsStorageView, EditStorageView, DeleteStorageView

urlpatterns = [
    path('', HomeStorageView.as_view(), name='home_storage'),
    path('choose', ChooseStorageView.as_view(), name='choose_storage'),
    path('details/<int:pk>', DetailsStorageView.as_view(), name='detail_storage'),
    path('edit/<int:pk>', EditStorageView.as_view(), name='edit_storage'),
    path('delete/<int:pk>', DeleteStorageView.as_view(), name='delete_storage'),
]