from django.urls import path
from .views import post_list, add_post, user_posts, post_view, post_edit, LikeView


urlpatterns = [
    path('post_list/', post_list, name='post_list'),
    path('add_post/', add_post, name='add_post'),
    path('user_posts/<int:user_id>/', user_posts, name='user_posts'),
    path('post_view/<int:post_id>/', post_view, name='post_view'),
    path('post_view/<int:post_id>/like/', LikeView.as_view(), name='like_form'),
    path('post_edit/<int:post_id>/', post_edit, name='post_edit'),
]


