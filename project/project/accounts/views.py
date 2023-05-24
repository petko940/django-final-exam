from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from project.accounts.forms import NewUserForm


# Create your views here.
class RegistrationView(CreateView):
    template_name = 'accounts/register.html'
    form_class = NewUserForm
    success_url = reverse_lazy('home')  # Redirect to the login page after successful registration

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return response

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect to home page or any other desired URL
        return super().dispatch(request, *args, **kwargs)
