# from django.contrib.auth.forms import UserCreationForm
# from registration.models import CustomUser
# from django import forms
#
#
# # from .models import User
# # from django.contrib.auth.decorators import login_required
#
#
# # @login_required
# class CustomUserCreationForm(UserCreationForm):
#     user = forms.ModelChoiceField(queryset=CustomUser.objects.all())  # Set the queryset here
#
#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ['username', 'email', 'password', 'password2']
#
# from django.contrib.auth.forms import AuthenticationForm
# from django import forms

# class CustomAuthenticationForm(AuthenticationForm):
#     pass
#     #user = forms.ModelChoiceField(queryset=CustomUser.objects.all())
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['user'].queryset = CustomUser.objects.all()

# from django.contrib.auth.forms import AuthenticationForm
#
# class CustomAuthenticationForm(AuthenticationForm):
#     pass