from django.urls import path
from main import views
urlpatterns = [
    path('',views.index.as_view(),name='index')
]