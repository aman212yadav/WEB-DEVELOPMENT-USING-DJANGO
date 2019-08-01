from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from auth import forms

# Create your views here.
def login(request):
    inputForm=forms.LoginForm()
    error=None
    if request.method=='POST' :
        inputForm=forms.LoginForm(request.POST)
        if inputForm.is_valid():
            username=inputForm.cleaned_data['username']
            password=inputForm.cleaned_data['password']
            user= authenticate( username=username , password=password)
            if user:
              return HttpResponseRedirect('')
            else:
              error='enter valid data'
    context={ 'form': inputForm, 'error':error}
    return render(request,'auth/loginform.html',context)            
