from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, CreateView, DeleteView, DetailView

from project.common.models import ShowPC
from project.cpus.models import ChosenCpus
from project.gpus.models import ChosenGpus
from project.motherboards.models import Motherboard
from project.ram.models import RAM
from project.storage.models import Storage


# Create your views here.
class HomeView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['show_pc'] = ShowPC.objects.annotate(num_likes=Count('likes')).order_by('-num_likes')
        return context


class ChoosePCToShowView(LoginRequiredMixin, CreateView):
    template_name = 'common/choose-pc.html'
    success_url = reverse_lazy('home')
    model = ShowPC
    fields = ['choose_cpu', 'choose_gpu', 'choose_ram', 'choose_motherboards', 'choose_storage']

    def set_components(self, form):
        components = {
            'choose_cpu': ChosenCpus,
            'choose_gpu': ChosenGpus,
            'choose_ram': RAM,
            'choose_motherboards': Motherboard,
            'choose_storage': Storage
        }
        for key, value in components.items():
            form.fields[key].queryset = value.objects.filter(user=self.request.user).exclude(showpc__isnull=False)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.initial['user'] = self.request.user.username
        self.set_components(form)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.username != kwargs['username']:
            return redirect("access_denied_view")
        return super().dispatch(request, *args, **kwargs)


class SelectedPCView(LoginRequiredMixin, TemplateView):
    template_name = 'common/pc.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_pcs'] = ShowPC.objects.filter(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        selected_pc_id = request.POST.get('selected_pc_id')
        if selected_pc_id:
            selected_pc = ShowPC.objects.filter(user=self.request.user, id=selected_pc_id)[0]
            if selected_pc:
                selected_pc.delete()
        return redirect('selected_pc', username=self.request.user.username)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.username != kwargs['username']:
            return redirect("access_denied_view")
        return super().dispatch(request, *args, **kwargs)


class DeleteSelectedPCView(LoginRequiredMixin, DeleteView):
    model = ShowPC

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})


@login_required
@require_POST
def like_pc(request, pc_id):
    pc = get_object_or_404(ShowPC, id=pc_id)
    user = request.user

    if user in pc.likes.all():
        pc.likes.remove(user)
    else:
        pc.likes.add(user)

    return redirect(request.META.get('HTTP_REFERER', 'home') + '#pc-' + str(pc.id))


