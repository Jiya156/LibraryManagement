from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    published_Year = models.IntegerField(max_length=50)
    availability = models.BooleanField(default=True)

# Create your models here.
