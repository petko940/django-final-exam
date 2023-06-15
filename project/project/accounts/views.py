from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView

from project.accounts.forms import RegistrationForm, LoginForm, UsernameChangeForm, AccountPasswordChangeForm


# Create your views here.
class RegistrationView(CreateView):
    template_name = 'accounts/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')

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
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class SignInView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    form_class = LoginForm


class Logout(LogoutView):
    pass


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"/login?next=/profile")
        return super().dispatch(request, *args, **kwargs)


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileUsernameChangeView(UpdateView):
    template_name = 'accounts/change-username.html'
    form_class = UsernameChangeForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"/login?next=/profile/change-username")
        return super().dispatch(request, *args, **kwargs)


class ProfilePasswordChangeView(PasswordChangeView):
    template_name = 'accounts/change-password.html'
    form_class = AccountPasswordChangeForm
    success_url = reverse_lazy('profile')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(f"/login?next=/profile/change-password")
        return super().dispatch(request, *args, **kwargs)
