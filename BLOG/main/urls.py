"""BLOG URL Configuration

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
from django.urls import path,include
from main import views
urlpatterns = [
  
    path('',views.index),
    path('home',views.index),
    path('article/<int:pk>',views.article,name='get_article'),
    path('author/<int:pk>',views.author,name='get_author'),
    path('article',views.create_article,name='create_article'),
    path('all_authors', views.all_authors,name="all_authors"),
    path('all_articles', views.all_articles,name="all_articles"),
    path('submit_article',views.submit_article,name='submit_article'),
    path('author',views.create_author,name='create_author'),
    path('submit_author', views.submit_author,name='submit_author')
]
