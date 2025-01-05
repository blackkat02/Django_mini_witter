from django.shortcuts import render, get_object_or_404, redirect
from registration.models import CustomUser
from .forms import CustomUserCreationForm, UserProfileForm
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.contrib.auth import logout
from django.views.generic import DetailView
from django.shortcuts import Http404
from .models import UserProfile

#from django.contrib.auth import login
#from django.contrib.auth.forms import AuthenticationForm
#from django.shortcuts import render, redirect
#from django.urls import reverse_lazy
#from django.views.generic import CreateView
#from .forms import CustomUserCreationForm

#from django.contrib.auth import login, authenticate
#from django.urls import reverse_lazy
#from django.views.generic import CreateView
#from .forms import CustomUserCreationForm

#from django.shortcuts import redirect
#from django.contrib.auth import login

class RegistrationView(CreateView):
    template_name = 'registration/registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('registration:user_list')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()

        # Authenticate the user after registration
        login(self.request, user)

        return super().form_valid(form)  # Redirect to success URL


# def registration(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             # Шифруємо пароль перед збереженням
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             # Redirect to a success page or any other desired page
#             return redirect(reverse_lazy('registration:user_list'))
#
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'registration/registration.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect(reverse_lazy('registration:user_list'))  # Redirect to user list page
        # If the form is invalid or authentication fails, render the login page again with errors.
        return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    """Logs out the user and redirects to the login page."""
    if request.user.is_authenticated:
        logout(request)
        return redirect('registration:user_list')  # Redirect to login
    else:
        return redirect('user_authentication_view')


def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'registration/user_list.html', {'users': users})


# def add_profile(request, user_id=None):
#     user = get_object_or_404(CustomUser, pk=user_id)
#     form = UserProfileForm(data=request.POST)
#         form.save()
#         return redirect('post_list')
#     else:
#         form = PostForm()
#     return render(request, 'registration/profile_info.html', {'form': form})
#
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile

@receiver(post_save, sender=get_user_model())
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=get_user_model())
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import UserProfileForm
from django.urls import reverse

class ProfileEdit(View):
    def get(self, request, user_id):
        user = CustomUser.objects.get(pk=user_id)
        form = UserProfileForm(instance=user.profile)
        return render(request, 'registration/profile_edit.html', {'form': form, 'user': user, 'user_id': user_id})

    def post(self, request, user_id):
        user = CustomUser.objects.get(pk=user_id)
        form = UserProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect(reverse('registration:profile_view', kwargs={'user_id': user_id}))
        return render(request, 'registration/profile_view.html', {'form': form, 'user': user, 'user_id': user_id})


class MyProfileView(DetailView):
    model = UserProfile
    template_name = 'registration/my_profile.html'
    context_object_name = 'my_profile'

    def get_object(self):
        # Return the profile of the current user
        return self.request.user.profile


# class ProfileView(DetailView):
#     model = UserProfile
#     template_name = 'registration/profile_view.html'
#     context_object_name = 'profile_view'
#
#     def get_object(self):
#         pk = self.kwargs.get('user_id')
#         if pk is not None:
#
#             username = user_id  # Assuming user_id represents the username
#             return UserProfile.objects.get(user__username=username)
#         else:
#             # Handle the case where user_id is None, such as fetching the current user's profile
#             # For example:
#             user = self.request.user
#             profile = user.profile  # Assuming UserProfile is related to the user model
#             return profile

from django.views.generic import DetailView
from .models import UserProfile

class ProfileView(DetailView):
  model = UserProfile
  template_name = 'registration/profile_view.html'

  def get_context_data(self, **kwargs):
      context = super(ProfileView, self).get_context_data(**kwargs)
      context['user'] = self.object.user
      context['user_id'] = self.object.user_id  # Access the user_id from the related User object
      return context

  def get_object(self, queryset=None, **kwargs):
      user_id = self.kwargs.get('user_id')
      try:
          return get_object_or_404(UserProfile, user_id=user_id)
      except Http404:
          # Handle the case where the profile doesn't exist (e.g., redirect to a generic error page)
          return self.request.user.profile


def profile_list(request):
    users = UserProfile.objects.all()
    return render(request, 'registration/profile_list.html', {'users': users})