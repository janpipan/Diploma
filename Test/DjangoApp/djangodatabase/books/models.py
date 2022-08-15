from functools import total_ordering
from pyexpat import model
from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list_author')
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    total_pages = models.IntegerField()
    rating = models.FloatField()
    isbn = models.CharField(max_length=13)
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('list_book')