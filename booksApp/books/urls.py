
from books.views import book_details
from django.urls import path
from django.contrib import admin
from django.contrib.auth.decorators import login_required


from books.views import (hello , welcome , landing , book_details , books_home , book_profile ,
                         contact_us ,About , books_index , book_show , book_delete ,
                         book_create , book_update,create_book_model_form , edit_book)
#include books urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld' , hello , name='hellopage'),
    path('wlcm' , welcome , name = 'welcomepage'),
    path('land' , landing , name = 'allbooks'),
    path('book/<int:id>' , book_details , name = 'book.details'),
    path('home' , books_home , name = "books.home"),
    path('old/<int:id>' , book_profile , name= 'books.profile'),
    path('contact' , contact_us , name = 'books.contact' ),
    path('about' , About , name ='books.about'),
    path('' , books_index , name = 'books.index'),
    path('<int:id>' , book_show , name= 'books.show'),
    path('<int:id>/delete' , book_delete , name = 'books.delete'),
    path('create' , book_create , name = 'books.create'),
    path('update/<int:id>' , book_update , name='books.update'),
    path('forms/createmodel' , create_book_model_form , name = 'book.createmodel'),
    path('forms/<int:id>/edit' ,login_required(edit_book) , name= 'books.edit')

]