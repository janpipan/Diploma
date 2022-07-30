from functools import total_ordering
from pyexpat import model
from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Books(models.Model):
    title = models.CharField(max_length=100)
    total_pages = models.IntegerField()
    rating = models.IntegerField()
    isbn = models.CharField(max_length=13)
    date = models.DateField()
    author = models.ManyToManyField(Author)

    def __str__(self):
        return self.title