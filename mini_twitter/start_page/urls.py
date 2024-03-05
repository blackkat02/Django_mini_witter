from django.urls import path
from .views import start_page
from posts.views import add_post

urlpatterns = [
    path('start_page/', start_page, name='start_page'),  # Змініть шлях на порожній рядок
]

