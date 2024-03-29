from django.urls import path

from project.common.views import HomeView, ChoosePCToShowView, SelectedPCView, DeleteSelectedPCView, like_pc

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/<username>/choose-pc/', ChoosePCToShowView.as_view(), name='choose_pc'),
    path('profile/<username>/selected-pc/', SelectedPCView.as_view(), name='selected_pc'),
    path('remove-pc/remove/<int:pk>/', DeleteSelectedPCView.as_view(), name='remove_pc'),

    path('like_pc/<int:pc_id>/', like_pc, name='like_pc'),
]
