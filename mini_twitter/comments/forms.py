from django import forms
from posts.models import Post
from .models import Comment
from registration.models import CustomUser


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content']
        widgets = {
            'user': forms.HiddenInput(), 'post': forms.HiddenInput()
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = CustomUser.objects.all()
        self.fields['post'].queryset = Post.objects.all()
