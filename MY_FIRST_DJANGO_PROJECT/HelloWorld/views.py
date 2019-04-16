from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    developed_by='Aman yadav'
    friends=[
        " Aman yadav",
        "Divyam",
        "Kunal",
        "Akash",
        "Anuj"
    ]
    context={
        "developer":developed_by,
        "friends":friends
    }
    response=render(request,'HelloWorld/index.html',context)
    return response
def hello(request):
    return render(request,'HelloWorld/hello.html');    
