from django.urls import path
from main import views

urlpatterns=[ path('',views.index,name='index'),
path('projects/',views.projects,name='projects'),
path('languages/',views.languages,name='languages')
]