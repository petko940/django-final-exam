from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView, DeleteView

from project.cpus.views import UserAccessMixin
from project.motherboards.forms import CreateMotherboardForm
from project.motherboards.models import Motherboard


# Create your views here.
class HomeMotherboardView(TemplateView):
    template_name = 'motherboards/motherboard.html'


class CreateMotherboardView(LoginRequiredMixin, CreateView):
    template_name = 'motherboards/choose-motherboard.html'
    form_class = CreateMotherboardForm
    success_url = reverse_lazy('home_motherboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DetailsMotherboardView(UserAccessMixin, LoginRequiredMixin, DetailView):
    template_name = 'motherboards/details-motherboard.html'
    model = Motherboard


class EditMotherboardView(UserAccessMixin, LoginRequiredMixin, UpdateView):
    template_name = 'motherboards/edit-motherboard.html'
    model = Motherboard
    form_class = CreateMotherboardForm

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})


class DeleteMotherboardView(UserAccessMixin, LoginRequiredMixin, DeleteView):
    template_name = 'motherboards/delete-motherboard.html'
    model = Motherboard

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
