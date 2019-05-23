from django.shortcuts import render ,get_object_or_404
from main import models 

# Create your views here.
def index(request):
    latest_articles=models.Article.objects.all().order_by('-createdAt')[:10]
    context={
        "latest_articles":latest_articles
    }
    return render(request,'main/index.html',context)

def article(request,pk):
    article=get_object_or_404(models.Article,pk=pk)
    context={
        'article':article
    }
    return render(request,'main/article.html',context)
def author(request,pk):
    author=get_object_or_404(models.Author,pk=pk)
    context={
        'author':author
    }
    return render(request,'main/author.html',context)   
def create_article(request):
    authors=models.Author.objects.all()
    context={"authors":authors}
    return render(request,'main/create_article.html',context)    
def submit_article(request):
    title=request.POST.get('title')
    content=request.POST.get('content')
    article_data={
        'title':title,
        'content':content
    }
    context={}
    article=models.Article.objects.create(**article_data)
    author=models.Author.objects.get(pk=request.POST.get('author'))
    article.authors.set([author])
    context['success']=True
    return render(request,'main/submit_article.html',context)
def all_authors(request):
    authors=models.Author.objects.all()
    context={
     'authors':authors
    }
    return render(request,'main/all_authors.html',context)
def all_articles(request):
    articles=models.Article.objects.all()
    context={
     'articles':articles
    }
    return render(request,'main/all_articles.html',context)    
def create_author(request):
    return render(request,'main/create_author.html',{}) 
def submit_author(request):
    name=request.POST.get('author')
    context={}
    author_data={
        'name':name
    }
    author=models.Author.objects.create(**author_data)
    context['success']=True
    return render(request,'main/submit_author.html',context)



