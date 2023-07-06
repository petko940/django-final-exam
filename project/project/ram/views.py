from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView

from project.ram.forms import RAMForm, DeleteRamForm
from project.ram.models import RAM


# Create your views here.
class HomeRamView(TemplateView):
    template_name = 'ram/ram.html'


class CreateRamView(LoginRequiredMixin, CreateView):
    template_name = 'ram/choose-ram.html'
    form_class = RAMForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RAMInformationView(LoginRequiredMixin, DetailView):
    template_name = 'ram/details-ram.html'
    model = RAM


class EditRamView(LoginRequiredMixin, UpdateView):
    template_name = 'ram/edit-ram.html'
    model = RAM
    form_class = RAMForm

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})


class DeleteRamView(DeleteView):
    template_name = 'ram/delete-ram.html'
    model = RAM

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
