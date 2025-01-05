from django import forms
from .models import Post, Like
from registration.models import CustomUser

#from django.contrib.auth.decorators import login_required


#@login_required
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['user', 'title', 'content']
        widgets = {
            'user': forms.HiddenInput(),  # Hide the user field in the form
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.all()

# class LikeForm(forms.ModelForm):
#     class Meta:
#         model = Like
#         fields = ['like', 'post']
#         exclude = ['user']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        fields = ['user', 'post']  # Adjust the fields as per your requirements

