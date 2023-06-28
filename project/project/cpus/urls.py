from django.urls import path

from project.cpus.views import HomeCpuView, ChooseCpuListView

urlpatterns = [
    path('', HomeCpuView.as_view(), name='home_cpu'),
    path('choose/', ChooseCpuListView.as_view(), name='choose_cpu'),
]
