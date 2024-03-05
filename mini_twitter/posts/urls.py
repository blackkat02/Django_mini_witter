from django.urls import path
from posts.views import post_list, add_post, user_posts, post_view


urlpatterns = [
    path('post_list/', post_list, name='post_list'),
    path('add_post/', add_post, name='add_post'),
    path('user_posts/<int:user_id>/', user_posts, name='user_posts'),
    path('post_view/<int:post_id>/', post_view, name='post_view'),
]


