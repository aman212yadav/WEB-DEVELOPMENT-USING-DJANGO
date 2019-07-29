from django.contrib import admin
from django.urls import path
from main.views import (index,collegeDetail,collgeList,collegeCreate,studentCreate,updateCollege,deleteStudent)
urlpatterns = [
    path('', index.as_view()),
    path('collegeDetail/<int:pk>',collegeDetail.as_view(),name='collegeDetail'),
    path('collegeList/',collgeList.as_view(),name='collegeList'),
    path('createCollege/',collegeCreate.as_view(),name='createCollege'),
    path('createStudent/',studentCreate.as_view(),name='createStudent'),
    path('updateCollege/<int:pk>', updateCollege.as_view(),name="updateCollege"),
    path('deleteStudent/<int:pk>',deleteStudent.as_view(),name='deleteStudent'),
  
]
