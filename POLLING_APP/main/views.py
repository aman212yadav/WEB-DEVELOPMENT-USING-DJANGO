from django.shortcuts import render
from django.views.generic import ListView
from main import models 
# Create your views here.

class index(ListView):
    model=models.Question
    template_name='main/index.html'
    context_object_name='questions'
