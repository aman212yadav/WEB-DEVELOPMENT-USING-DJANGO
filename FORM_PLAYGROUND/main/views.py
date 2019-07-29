from django.shortcuts import render
from main import forms

# Create your views here.
def index(request):
    context={
        'form':forms.ExampleForm
    }
    return render(request,'index.html',context)
