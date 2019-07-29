from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
def index(request):
    context={'NAME':settings.DATA['NAME'],
             'ABOUT_ME':settings.DATA['ABOUT_ME']
             }
    return render(request,'main/index.html',context)
def showLanguages(request):
    context={}
    context['languages']=settings.DATA['LANGUAGES']
    return render(request,'main/languages.html',context)    
def showProjects(request):
    context={'PROJECTS':settings.DATA['PROJECTS']}
    return render(request,'main/projects.html',context)    

