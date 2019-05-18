from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def analyze(request):
    djText=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    capitalizefirst=request.POST.get('capitalizefirst','off')
    newlineremover=request.POST.get('newlineremover','off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if removepunc=='on':
        analysed=''
        for char in djText:
            if char not in punctuations:
                analysed=analysed+char
        params={'purpose':'removed punctuation','analysed_text':analysed}
        djText=analysed
      
    if capitalizefirst=='on':
        analysed=''
        for char in djText.split(' '):
            analysed+=char.upper()
        params={'purpose':'capitalize first','analysed_text':analysed}
        djText=analysed
       
    if newlineremover=='on':
        analysed=''
        for char in djText:
            if char!='\n' and char !='\r':
                analysed+=char
        params={'purpose':'removed Newline','analysed_text':analysed}
        djText=analysed
            
    if newlineremover !='on' and capitalizefirst !='on' and removepunc=='on' :
        return HttpResponse(' Error ')      
    return render(request,'analyze.html',params)            

