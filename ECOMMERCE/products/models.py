from django.db import models
import os,random

# Create your models here.

def get_file_path(isinstance,filename):
    name,extension = os.path.splitext(filename)
    newname=random.randint(1,9999999999)
    return 'products/'+str(newname)+'/'+str(newname)+str(extension)

class Product(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField()
    price=models.DecimalField(decimal_places=2,max_digits=40,null=True,blank=True)
    image=models.ImageField(upload_to=get_file_path)

    def __str__(self):
        return self.title
