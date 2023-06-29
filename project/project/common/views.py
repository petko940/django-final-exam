from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from project.cpus.models import ChosenCpus


# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     try:
    #         context['cpus'] = ChosenCpus.objects.filter(user=self.request.user)
    #     except:
    #         pass
    #     return context
