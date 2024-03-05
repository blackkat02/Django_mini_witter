from django.urls import path, include
from .views import user_list, user_info


urlpatterns = [
    path('user_list/', user_list, name='user_list'),
    path('user_info/<int:user_id>/', user_info, name='user_info'),
]