from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from api import serializers , models
import json

class Student:
    name='Aman'
    roll=1
    marks=98
@api_view()
def usersApi(request):
    student=Student()
    response=serializers.StudentSerializers(student)
    return Response(response.data)

@api_view()
def articlesApi(request):
    articles= models.Article.objects.all()
    response=serializers.ArticleSerializers(articles,many=True)
    return Response(response.data)

@api_view(['POST'])    
def createArticleApi(request):
 
    body= json.loads(request.body)
    
    response=serializers.ArticleSerializers(data=body)
    if response.is_valid():
        inst=response.save()
        response=serializers.ArticleSerializers(inst)
        return Response(response.data)
    return Response(response.errors)

