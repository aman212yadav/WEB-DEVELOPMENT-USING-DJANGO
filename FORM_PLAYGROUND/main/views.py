from django.shortcuts import render
from main import forms
from main.models import Student
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    context={
        'form':forms.ExampleForm
    }
    return render(request,'index.html',context)
def students(request):
    students=Student.objects.all()
    context={"students":students}
    return render(request,'student.html',context)
def addStudent(request):
    form=forms.StudentForm()
    if request.POST:
        form=forms.StudentForm(request.POST)
        if form.is_valid():
            form.save()
            HttpResponseRedirect('/student')
    context={'studentForm':form}
    return render(request,'addStudent.html',context)        



