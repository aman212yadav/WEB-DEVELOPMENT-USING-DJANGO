from django.urls import path
from HelloWorld import views
urlpatterns = [
    path('',views.index)
]