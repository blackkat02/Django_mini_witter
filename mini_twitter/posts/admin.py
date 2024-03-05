# mini_twitter/admin.py
from django.contrib import admin
from users.models import User
from posts.models import Post
from comments.models import Comment

admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)

