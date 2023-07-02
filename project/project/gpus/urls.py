from django.urls import path

from project.gpus.views import HomeGpuView, ChooseGpuListView, GpuDetailsView, DeleteGpuView

urlpatterns = [
    path('', HomeGpuView.as_view(), name='home_gpu'),
    path('choose/', ChooseGpuListView.as_view(), name='choose_gpu'),
    path('details/<int:pk>/',  GpuDetailsView.as_view(), name='detail_gpu'),
    path('delete/<int:pk>/',  DeleteGpuView.as_view(), name='delete_gpu'),
]
