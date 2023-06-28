from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from project.cpus.forms import ChooseCpuListForm
from project.cpus.models import AllCpus


class HomeCpuView(TemplateView):
    template_name = 'cpus/cpu.html'


class ChooseCpuListView(ListView):
    model = AllCpus
    template_name = 'cpus/choose-cpu.html'
    context_object_name = 'cpus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ChooseCpuListForm()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        brand = self.request.GET.get('brand')
        name = self.request.GET.get('name')
        cores = self.request.GET.get('cores')
        threads = self.request.GET.get('threads')
        max_turbo_frequency = self.request.GET.get('max_turbo_frequency')
        base_frequency = self.request.GET.get('base_frequency')
        tdp = self.request.GET.get('tdp')

        if brand:
            queryset = queryset.filter(brand__icontains=brand)

        if name:
            queryset = queryset.filter(name__icontains=name)

        if cores:
            cores = int(cores)
            queryset = queryset.filter(cores=cores)

        if threads:
            queryset = queryset.filter(threads__icontains=threads)

        if max_turbo_frequency:
            queryset = queryset.filter(max_turbo_frequency__icontains=max_turbo_frequency)

        if base_frequency:
            queryset = queryset.filter(base_frequency__startswith=base_frequency)

        if tdp:
            queryset = queryset.filter(tdp=tdp)

        if len(queryset) == 2666:
            queryset = AllCpus.objects.none()
        print(len(queryset))

        return queryset
