from django import forms
from .models import User
#from django.contrib.auth.decorators import login_required


#@login_required
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'email', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all()
