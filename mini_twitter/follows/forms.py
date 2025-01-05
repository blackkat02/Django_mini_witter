from django import forms
from .models import Follower

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follower
        fields = ['user', 'followed_user']