from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

from project.storage.forms import ChooseStorageForm
from project.storage.models import Storage


# Create your views here.
class HomeStorageView(TemplateView):
    template_name = 'storage/storage.html'


class ChooseStorageView(LoginRequiredMixin, CreateView):
    template_name = 'storage/choose_storage.html'
    form_class = ChooseStorageForm
    success_url = reverse_lazy('home_storage')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DetailsStorageView(LoginRequiredMixin, DetailView):
    template_name = 'storage/details-storage.html'
    model = Storage


class EditStorageView(LoginRequiredMixin, UpdateView):
    template_name = 'storage/edit-storage.html'
    model = Storage
    form_class = ChooseStorageForm

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})


class DeleteStorageView(LoginRequiredMixin, DeleteView):
    template_name = 'storage/delete-storage.html'
    model = Storage

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
