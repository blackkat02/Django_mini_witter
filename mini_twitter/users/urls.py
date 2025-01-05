from django.urls import path, include
from django.shortcuts import render
from .views import user_info#, user_list #, RegisterView$, login_user_view # CustomLoginView#, CsrfFailureView


urlpatterns = [
    #path('user_list/', user_list, name='user_list'),
    path('user_info/<int:user_id>/', user_info, name='user_info'),
    #path('register/', RegisterView.as_view(), name='register'),
    #path('login/', CustomLoginView.as_view(), name='login'),
    #path('csrf_failure/', CsrfFailureView.as_view(), name='csrf_failure'),
]