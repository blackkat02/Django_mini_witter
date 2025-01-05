from django.db import models
from registration.models import UserProfile

class Follower(models.Model):
    user = models.ForeignKey(UserProfile, related_name='follower', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(UserProfile, related_name='following', on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'followed_user')
