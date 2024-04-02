
from books.views import book_details
from django.urls import path
from django.contrib import admin


from books.views import (hello , welcome , landing , book_details , books_home , book_profile , contact_us ,About)
#include books urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld' , hello , name='hellopage'),
    path('wlcm' , welcome , name = 'welcomepage'),
    path('land' , landing , name = 'allbooks'),
    path('book/<int:id>' , book_details , name = 'book.details'),
    path('home' , books_home , name = "books.home"),
    path('<int:id>' , book_profile , name= 'books.profile'),
    path('contact' , contact_us , name = 'books.contact' ),
    path('about' , About , name ='books.about')
]