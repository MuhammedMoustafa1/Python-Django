from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    num_of_pages = models.IntegerField(null=True ,blank=True)
    author = models.CharField(max_length=100 , null=True , blank=True)
    price = models.IntegerField(null=True , blank=True)
    image = models.CharField(max_length=200 , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True , null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.title}'

    @property
    def show_url(self):
        url = reverse('books.show' , args=[self.id])
        return url





