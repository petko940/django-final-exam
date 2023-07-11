from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from project.common.forms import ShowPCForm
from project.cpus.models import ChosenCpus


# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'


class ShowPCView(LoginRequiredMixin, CreateView):
    template_name = 'accounts/choose-pc.html'
    form_class = ShowPCForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user_id = self.request.user.id
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.username != kwargs['username']:
            return redirect("access_denied_view")
        return super().dispatch(request, *args, **kwargs)
