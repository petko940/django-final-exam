from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, FormView

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
        username = form.cleaned_data.get('username').lower()
        password = form.cleaned_data.get('password1')
        user = get_user_model()
        user.objects.filter(username=self.object.username).update(username=username)

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
    success_url = reverse_lazy('home')


class Logout(LogoutView):
    pass


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('home')
    redirect_to = "/login?next=/profile/delete"

    def get_object(self, queryset=None):
        return self.request.user


class ProfileUsernameChangeView(LoginRequiredMixin, UpdateView):
    form_class = UsernameChangeForm
    template_name = 'accounts/change-username.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user


class ProfilePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change-password.html'
    form_class = AccountPasswordChangeForm
    success_url = reverse_lazy('profile')
