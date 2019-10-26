from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login ,logout
from django.contrib import messages
from accounts.forms import UserRegistrationForm
from django.contrib.auth.models import User

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            request_url=request.GET.get('next','home')
            return redirect(request_url)
        else:
            messages.error(request,'enter correct username and password')      
    return render(request,'accounts/login.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))  

def user_registration(request):
    
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            email=form.cleaned_data['email']
            user=User.objects.create_user(username=username,email=email,password=password)
            messages.success(request,'thanks for registering {}'.format(user.username))
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form=UserRegistrationForm()
    return render(request,'accounts/register.html',{'form':form})
