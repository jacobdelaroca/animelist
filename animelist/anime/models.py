from django.db import models
from django.contrib import admin

# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=200)
    rating = models.IntegerField()
    favorite = models.BooleanField()
    comment = models.CharField(max_length=1000)

admin.site.register(Anime)