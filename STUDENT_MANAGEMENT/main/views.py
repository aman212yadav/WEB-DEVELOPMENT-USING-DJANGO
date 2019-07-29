from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (DeleteView,DetailView,ListView,CreateView,UpdateView)
from django.views import View
from main import models
class index(View):
    def get(self,request):
        return HttpResponse("voila u have learnt Views")

class collegeDetail(DetailView):
    model=models.College
    template_name='college_detail.html'
    context_object_name='college'
class collgeList(ListView):
    model=models.College
    template_name='college_list.html'
    context_object_name='colleges'
class collegeCreate(CreateView):
    model=models.College
    fields='__all__'
    context_object_name='form'
    template_name='college_create.html'
    success_url='/collegeList'   
class studentCreate(CreateView):
    model=models.Student
    fields='__all__'
    context_object_name='form'
    template_name='student_create.html'
    success_url='/collegeList'  
class updateCollege(UpdateView):
    model=models.College
    fields='__all__'
    context_object_name='form'
    template_name='college_create.html'
    success_url='/collegeList'
class deleteStudent(DeleteView):
    model=models.Student
    template_name='confirm.html'
    success_url='/'             


