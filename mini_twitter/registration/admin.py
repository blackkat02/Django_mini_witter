from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from registration.models import CustomUser
from posts.models import Post
from comments.models import Comment

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Post)
admin.site.register(Comment)
