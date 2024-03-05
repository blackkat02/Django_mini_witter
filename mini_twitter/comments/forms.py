from django import forms
from posts.models import Post
from .models import Comment
from users.models import User


# from django.contrib.auth.decorators import login_required


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'post', 'content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all()
        self.fields['post'].queryset = Post.objects.all()
