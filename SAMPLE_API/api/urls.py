from django.urls import path
from api import views
urlpatterns = [
    path('users/', views.usersApi),
    path('articles/', views.articlesApi),
    path('createArticle',views.createArticleApi)
]
