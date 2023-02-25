"""yatube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import include, path
# from . import views

urlpatterns = [
    path('', include('posts.urls', namespace='index')),
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls', namespace='users')),
    path('auth/', include('django.contrib.auth.urls')),
    path('about/', include('about.urls', namespace='about')),
    path('create/', include('posts.urls', namespace='posts')),
    path('profile/', include('posts.urls', namespace='profile')),
]


# path('profile/', include('posts.urls', namespace='posts')),
# path('create/', include('posts.urls', namespace='posts')),
# path('posts/', include('posts.urls', namespace='posts')),
# path('group/', include('posts.urls', namespace='posts')),