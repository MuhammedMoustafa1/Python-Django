from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    num_of_pages = models.IntegerField(null=True ,blank=True)
    author = models.CharField(max_length=100 , null=True , blank=True)
    price = models.IntegerField(null=True , blank=True)
    image = models.CharField(max_length=200 , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True , null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)





