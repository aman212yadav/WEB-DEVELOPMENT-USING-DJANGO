from rest_framework import serializers
from api import models
class StudentSerializers(serializers.Serializer):
    name=serializers.CharField(max_length=256)
    roll=serializers.IntegerField()
    marks=serializers.IntegerField()



class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Tag
        fields='__all__'

class ArticleSerializers(serializers.ModelSerializer):
    tags=TagSerializers(many=True,read_only=True)
    class Meta:
        model=models.Article
        fields='__all__'

