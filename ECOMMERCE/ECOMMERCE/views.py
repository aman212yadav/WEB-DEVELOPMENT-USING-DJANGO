from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import ContactForm,LoginForm

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