from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .forms import ContactForm,LoginForm,RegisterForm

def login_page(request):
    login_form=LoginForm(request.POST or None)
    if request.method=='POST':
        if login_form.is_valid():
            print('1',request.user.is_authenticated)
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                print('2',request.user.is_authenticated)
            else:
                print("Error")   
        print(request.POST)
    context={
        "title":"login page",
        "form":login_form
    }    
    return render(request,"auth/login_page.html",context)
def register_page(request):
    form=RegisterForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            user=User.objects.create_user(username=username,email=email,password=password)
            if user is not None:
                login(request,user)
                redirect("/")

    context={
        'form':form,
        'title':"register page"
    }
    return render(request,"auth/register_page.html",context)        


def home_page(request):
    return render(request,"home_page.html",{})

def contact_page(request):
    form=ContactForm(request.POST or None)
    if request.method=='POST':
        print(request.POST)
    
    context={
          "title":"contact page",
          "form":form
      }
    return render(request,"contact/view.html", context)

def about_page(request):
    return render(request,"home_page.html",{})    