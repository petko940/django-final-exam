from django.urls import path

from project.common.views import HomeView, ShowPCView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/<username>/choose-pc/', ShowPCView.as_view(), name='choose_pc'),
]
