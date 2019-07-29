from django.contrib import admin
from django.urls import path,include
from main import views
urlpatterns = [
    path('', views.index,name="forms"),
    path('student',views.students),
    path('addStudent',views.addStudent)
    
]
