from django.urls import path
#from posts.views import post_list, add_post, user_posts, post_view
from .views import comment_list_for_user, comment_list, comment_list_for_post, add_comment_form
from .views import edit_comment, delete_comment

urlpatterns = [
    path('comment_list/', comment_list, name='comment_list'),
    path('comment_list_for_user/<int:user_id>/', comment_list_for_user, name='comment_list_for_user'),
    path('comment_list_for_post/<int:post_id>/', comment_list_for_post, name='comment_list_for_post'),
    path('add_comment_form/<int:post_id>/', add_comment_form, name='add_comment_form'),
    path('edit_comment/<int:comment_id>/', edit_comment, name='edit_comment'),
    path('delete_comment/<int:comment_id>/', delete_comment, name='delete_comment'),
]


#path('posts/<int:post_id>/add_comment/', add_comment_form, name='add_comment_form'),