from django.shortcuts import render
from django.contrib.auth.views import LoginView , LogoutView

class Login(LoginView):
    template_name='auth/index.html'
    redirect_authenticated_user=True
    next_page ='base.html'
class Logout(LogoutView):
    pass    


