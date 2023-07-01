from django.urls import path

from project.gpus.views import HomeGpuView

urlpatterns = [
    path('', HomeGpuView.as_view(), name='home_gpu'),
]
