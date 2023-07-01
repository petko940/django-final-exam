from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeGpuView(TemplateView):
    template_name = 'gpus/gpu.html'
