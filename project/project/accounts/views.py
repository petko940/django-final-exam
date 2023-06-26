from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views.generic import CreateView, TemplateView, DeleteView, UpdateView, FormView, DetailView, RedirectView

from project.accounts.forms import RegistrationForm, LoginForm, UsernameChangeForm, AccountPasswordChangeForm
from project.accounts.models import ExtendedUser


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

        user = User.objects.get(username=username)
        ExtendedUser.objects.create(user=user)

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


class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'accounts/profile.html'
    model = ExtendedUser

    def get_object(self, queryset=None):

        if 'slug' in self.kwargs:
            slug = self.kwargs['slug']
            return get_object_or_404(self.model, slug=slug)
        else:
            return self.request.user.extended_user


class DeleteProfileView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'accounts/delete.html'
    success_url = reverse_lazy('home')
    redirect_to = "/login?next=/profile/delete"

    def get_object(self, queryset=None):
        return self.request.user


# class ProfileUsernameChangeView(LoginRequiredMixin, UpdateView):
#     form_class = UsernameChangeForm
#     template_name = 'accounts/change-username.html'
#     success_url = reverse_lazy('profile_no_slug')
#
#     def get_object(self, queryset=None):
#         return self.request.user

def profile_username_change_view(request, slug=None):
    form = UsernameChangeForm()

    if request.method == 'POST':
        form = UsernameChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            extended_user = get_object_or_404(ExtendedUser, slug=slug)
            extended_user.slug = slugify(extended_user.user.username)
            extended_user.save()
            return redirect('profile', slug=extended_user.slug)

    context = {
        'form': form
    }
    return render(request, 'accounts/change-username.html', context)


class ProfilePasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change-password.html'
    form_class = AccountPasswordChangeForm
    # success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse_lazy('profile', kwargs={'slug': self.request.user.extended_user.slug})

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['slug'] = self.request.user.profile.slug
    #     return context
