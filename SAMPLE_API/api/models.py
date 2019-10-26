from django.db import models

# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=256)
    def __str__(self):
        return self.name


class Article(models.Model):
    slug=models.SlugField(null=False,blank=False)
    title=models.CharField(max_length=256)
    description=models.TextField(max_length=256)
    body=models.TextField(max_length=256)
    tags=models.ManyToManyField('Tag',blank=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now_add=True)
    favorited=models.BooleanField()
    favoritesCount=models.IntegerField(default=0)

