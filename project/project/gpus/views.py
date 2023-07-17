from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, DeleteView

from project.gpus.forms import ChooseGpuForm
from project.gpus.models import AllGpus, ChosenGpus


# Create your views here.
class HomeGpuView(TemplateView):
    template_name = 'gpus/gpu.html'


class ChooseGpuListView(LoginRequiredMixin, ListView):
    model = AllGpus
    template_name = 'gpus/choose-gpu.html'
    context_object_name = 'gpus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ChooseGpuForm(data=self.request.GET)
        context['sort_order'] = self.request.GET.get('sort_order')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        sort_by = self.request.GET.get('sort_by')
        sort_order = self.request.GET.get('sort_order')

        filter_params = {
            'manufacturer__icontains': self.request.GET.get('manufacturer'),
            'name__icontains': self.request.GET.get('name'),
            'release_year': self.request.GET.get('release_year'),
            'memory_size': self.request.GET.get('memory_size'),
            'gpu_clock': self.request.GET.get('gpu_clock'),
            'memory_clock': self.request.GET.get('memory_clock'),
            'memory_type__icontains': self.request.GET.get('memory_type'),
        }

        for param, value in filter_params.items():
            if value:
                queryset = queryset.filter(**{param: value})

        if not any(filter_params.values()):
            queryset = AllGpus.objects.none()

        if sort_by is not None:
            queryset = queryset.order_by(
                F(sort_by).asc(nulls_last=True) if sort_order == 'asc' else F(sort_by).desc(nulls_last=True))

        return queryset

    def post(self, request, *args, **kwargs):
        gpu_id = self.request.POST.get('gpu_id')
        gpu = AllGpus.objects.get(id=gpu_id)
        user = self.request.user

        chosen_gpu = ChosenGpus(
            user=user,
            chosen_gpu=gpu)

        chosen_gpu.save()
        return redirect('home_gpu')


class GpuDetailsView(DetailView):
    template_name = 'gpus/details-gpu.html'
    model = ChosenGpus

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        chosen_gpu = self.get_object().chosen_gpu

        gpu = AllGpus.objects.get(id=chosen_gpu.id)
        context['gpu_details'] = gpu

        return context


class DeleteGpuView(DeleteView):
    model = ChosenGpus
    template_name = 'gpus/delete-gpu.html'

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
