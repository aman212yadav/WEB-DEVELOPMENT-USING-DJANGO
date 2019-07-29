from django.contrib import admin
from django.urls import path
from main import views
urlpatterns = [
    path('', views.index,name='home'),
    path('languages/', views.showLanguages,name='showLanguages'),
    path('projects/', views.showProjects,name='showProjects')
]
