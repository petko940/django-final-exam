from django.urls import path

from project.cpus.views import HomeCpuView, ChooseCpuListView, BuildCustomCpuView, DeleteCpuView, CpuInformationView

urlpatterns = [
    path('', HomeCpuView.as_view(), name='home_cpu'),
    path('choose/', ChooseCpuListView.as_view(), name='choose_cpu'),
    path('build-custom/', BuildCustomCpuView.as_view(), name='build_cpu'),
    path('details/<int:pk>/', CpuInformationView.as_view(), name='detail_cpu'),
    path('cpu/<int:pk>/delete/', DeleteCpuView.as_view(), name='delete_cpu'),
]
