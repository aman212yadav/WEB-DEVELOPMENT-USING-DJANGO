from django.contrib import admin

# Register your models here.
from main import models
admin.site.register([models.Author,models.Article])