from django.contrib import admin
from relationship_playground import models
# Register your models here.
admin.site.register([models.Author,models.Article,models.Pizza,models.Topping])
