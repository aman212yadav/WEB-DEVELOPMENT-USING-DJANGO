from django.db import models

class Student(models.Model):
    p=(('g','gender'),('f','female'),('u','undisclosed'))
    name=models.CharField(max_length=230)
    roll_No=models.IntegerField()
    gender=models.CharField(max_length=1,choices=p)

