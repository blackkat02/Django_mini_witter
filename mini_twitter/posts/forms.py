from django import forms
from posts.models import Post
from users.models import User
#from django.contrib.auth.decorators import login_required


#@login_required
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'user']  # Додаємо поле user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.all()
