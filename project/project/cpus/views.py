from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, DetailView

from project.cpus.forms import ChooseCpuListForm, DeleteCpuForm, CustomCpuForm
from project.cpus.models import AllCpus, ChosenCpus, CustomCpu


class HomeCpuView(TemplateView):
    template_name = 'cpus/cpu.html'


class ChooseCpuListView(LoginRequiredMixin, ListView):
    model = AllCpus
    template_name = 'cpus/choose-cpu.html'
    context_object_name = 'cpus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ChooseCpuListForm(data=self.request.GET or None)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_params = {
            'brand__icontains': self.request.GET.get('brand'),
            'name__icontains': self.request.GET.get('name'),
            'cores': self.request.GET.get('cores'),
            'threads__icontains': self.request.GET.get('threads'),
            'max_turbo_frequency__icontains': self.request.GET.get('max_turbo_frequency'),
            'base_frequency__startswith': self.request.GET.get('base_frequency'),
            'tdp': self.request.GET.get('tdp')
        }

        for param, value in filter_params.items():
            if value:
                queryset = queryset.filter(**{param: value})

        if not any(filter_params.values()):
            queryset = AllCpus.objects.none()

        return queryset

    def post(self, request, *args, **kwargs):
        cpu_id = self.request.POST.get('cpu_id')
        cpu = AllCpus.objects.get(id=cpu_id)
        user = self.request.user

        chosen_cpu = ChosenCpus(
            user=user,
            chosen_cpu=cpu,
            build_custom_cpu=None)

        chosen_cpu.save()
        return redirect('home')


class BuildCustomCpuView(LoginRequiredMixin, CreateView):
    model = CustomCpu
    template_name = 'cpus/custom-cpu.html'
    form_class = CustomCpuForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        cpu = form.save(commit=False)
        cpu.save()

        user = self.request.user

        chosen_cpu = ChosenCpus(
            user=user,
            build_custom_cpu=cpu,
            chosen_cpu=None
        )

        chosen_cpu.save()

        return super().form_valid(form)


class CpuInformationView(DetailView):
    template_name = 'cpus/details-cpu.html'
    model = ChosenCpus

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cpu_info'] = None
        context['custom_cpu_info'] = None

        chosen_cpu = self.get_object().chosen_cpu_id
        build_custom_cpu = self.get_object().build_custom_cpu_id

        if chosen_cpu:
            cpu = AllCpus.objects.get(id=chosen_cpu)
            context['cpu_info'] = cpu
        elif build_custom_cpu:
            custom_cpu = CustomCpu.objects.get(id=build_custom_cpu)
            context['custom_cpu_info'] = custom_cpu

        return context


class DeleteCpuView(DeleteView):
    model = ChosenCpus

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
