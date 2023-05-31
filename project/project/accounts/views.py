from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView, FormView

from project.accounts.forms import RegistrationForm, LoginForm


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


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
        if not request.user.is_authenticated:  # Check if user is not logged in
            return redirect(f"login?next=/profile")  # Redirect to login with desired profile URL
        return super().dispatch(request, *args, **kwargs)

# class ProfileChangeUsernameView(FormView):
#     template_name = 'accounts/change-username.html'
#     form_class = UsernameChangeForm
#     success_url = reverse_lazy('profile')  # Redirects to the same page after successful username change
#
#     def get_form_kwargs(self):
#         kwargs = super().get_form_kwargs()
#         kwargs['user'] = self.request.user
#         return kwargs
#
#     def form_valid(self, form):
#         new_username = form.cleaned_data['new_username']
#         user = self.request.user
#         user.username = new_username
#         user.save()
#         return super().form_valid(form)
