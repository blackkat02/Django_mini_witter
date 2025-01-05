"""
URL configuration for mini_twitter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from typing import List, Any

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from start_page import views as start_page_views



urlpatterns = [
    path('', start_page_views.start_page, name='start_page'),
    path('admin/', admin.site.urls),
    path('registration/', include('registration.urls')),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('comments/', include('comments.urls')),
    path('start_page/', include('start_page.urls')),
    path('follows/', include('follows.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)