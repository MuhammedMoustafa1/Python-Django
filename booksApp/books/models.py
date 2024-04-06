from django.db import models
from django.shortcuts import reverse , get_object_or_404
from categories.models import Category

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100 , blank=True)
    num_of_pages = models.IntegerField( blank=True)
    author = models.CharField(max_length=100 , blank=True)
    price = models.IntegerField(  blank=True)
    image = models.ImageField(upload_to="books/images" , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True , null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True , blank=True,
                                 related_name="allbooks")

    def __str__(self):
        return f'{self.title}'

    @property
    def show_url(self):
        url = reverse('books.show' , args=[self.id])
        return url

    @property
    def delete_url(self):
        url = reverse('books.delete', args=[self.id])
        return url

    @property
    def image_url(self):
        return f"/media/{self.image}"

    @property
    def update_url(self):
        return reverse('books.update', args=[self.id])

    @property
    def edit_url(self):
        url = reverse('books.edit' , args=[self.id])
        return url

    @classmethod
    def get_book_by_id(cls , id):
        return get_object_or_404(cls , pk=id)








