from django.db import models

# Create your models here.
class College(models.Model):
    collegeName =models.CharField(max_length=256)
    def __str__(self):
        return self.collegeName

class Student(models.Model):
    name=models.CharField(max_length=256)
    roll_no=models.IntegerField(unique=True)
    collegeName= models.ForeignKey('College',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
