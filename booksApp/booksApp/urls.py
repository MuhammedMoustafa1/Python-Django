"""
URL configuration for booksApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

from books.views import hello , welcome , landing , book_details

urlpatterns = [

    # specify part of the url --> variable must be integer
    # path('book/<int:id>' , book_details , name = 'book.details')
    #include books urls file in main url
    path('books/', include('books.urls')),
    path('categories/', include('categories.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/' , include('accounts.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
