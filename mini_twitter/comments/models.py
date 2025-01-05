from django.db import models
from registration.models import CustomUser
from posts.models import Post


# from django.contrib.auth.models import User

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Post Comment'
        verbose_name_plural = 'Post Comments'

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
