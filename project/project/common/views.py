from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['user'] = self.request.user

        return context
