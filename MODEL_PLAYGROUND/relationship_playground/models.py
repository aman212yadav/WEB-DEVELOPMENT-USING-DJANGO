from django.db import models
from django.core.validators import  MinValueValidator
# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=256)
    designation=models.CharField(max_length=256)
    def __str__(self):
        return self.name   
class Article(models.Model):
    title=models.CharField(max_length=256)
    body=models.TextField()
    author=models.ForeignKey('Author',on_delete=models.CASCADE)
    def __str__(self):
         return self.title    

class Topping(models.Model):
    name=models.CharField(max_length=256)
    def __str__(self):
        return self.name      
class Pizza(models.Model):
    name=models.CharField(max_length=256)
    price=models.IntegerField(validators=[MinValueValidator(0)])    
    toppings=models.ManyToManyField('Topping')
    def __str__(self):
        return self.name   

        
