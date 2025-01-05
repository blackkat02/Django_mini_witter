from django.urls import path
from .views import follower_list, following_list, follow_user


urlpatterns = [
    path('follower_list/<int:user_id>/', follower_list, name='follower_list'),
    path('following_list/<int:user_id>/', following_list, name='following_list'),
    path('follow_user/<int:user_id>/', follow_user, name='follow_user'),
]