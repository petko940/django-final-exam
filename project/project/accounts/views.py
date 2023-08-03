from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView

from project.accounts.forms import RegistrationForm, LoginForm, UsernameChangeForm, AccountPasswordChangeForm
from project.cpus.models import ChosenCpus
from project.gpus.models import ChosenGpus
from project.motherboards.models import Motherboard
from project.ram.models import RAM
from project.storage.models import Storage


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


class ProfileView(DetailView):
    template_name = 'accounts/profile.html'
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile_user = User.objects.get(username=self.kwargs['username'])
        context['cpus'] = ChosenCpus.objects.filter(user=profile_user)
        context['gpus'] = ChosenGpus.objects.filter(user=profile_user)
        context['rams'] = RAM.objects.filter(user=profile_user)
        context['storages'] = Storage.objects.filter(user=profile_user)
        context['motherboards'] = Motherboard.objects.filter(user=profile_user)
        return context


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def profile_username_change_view(request, username):
    check_username = request.user.username
    if check_username != username:
        return redirect("access_denied_view")

    form = UsernameChangeForm()

    if request.method == 'POST':
        form = UsernameChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile', username=request.user.username)

    context = {
        'form': form
    }
    return render(request, 'accounts/change-username.html', context)


def access_denied_view(request):
    return render(request, 'accounts/access_denied.html')


class ProfilePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change-password.html'
    form_class = AccountPasswordChangeForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if self.request.user.username != kwargs['username']:
            return redirect("access_denied_view")
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'username': self.request.user.username})
