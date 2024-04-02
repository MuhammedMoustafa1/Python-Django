from django.shortcuts import render , get_object_or_404 , redirect , reverse
from django.http import HttpResponse
from django.template import Template

from books.models import Book
# Create your views here.

#function views

def hello(request): ## accept http request
    """reply with http response"""
    print(request)
    return HttpResponse("We are here")

def welcome(request):
    name = "mohamed"
    return HttpResponse(f"<h1 style='color:red'>Welcome {name}</h1>")




books = [
    {"id": 1, "title": "To Kill a Mockingbird", "num_of_pages": 281, "author": "Harper Lee", "price": 12.99, "image": "1.png"},
    {"id": 2, "title": "1984", "num_of_pages": 328, "author": "George Orwell", "price": 9.99, "image": "2.png"},
    {"id": 3, "title": "Pride and Prejudice", "num_of_pages": 279, "author": "Jane Austen", "price": 8.99, "image": "3.png"},
    {"id": 4, "title": "The Great Gatsby", "num_of_pages": 180, "author": "F. Scott Fitzgerald", "price": 10.50, "image": "4.png"},
    {"id": 5, "title": "To Kill a Mockingbird", "num_of_pages": 324, "author": "Harper Lee", "price": 11.25, "image": "1.png"},
    {"id": 6, "title": "The Catcher in the Rye", "num_of_pages": 277, "author": "J.D. Salinger", "price": 10.99, "image": "2.png"},
    {"id": 7, "title": "The Hobbit", "num_of_pages": 310, "author": "J.R.R. Tolkien", "price": 14.99, "image": "3.png"}
]

def landing(request):
    return HttpResponse(books)

def book_details(request , id):
    print(type(id))
    #id = int(id)
    filtered_books = filter(lambda book: book['id'] == id , books) # filter object
    print(filtered_books)
    allBooks = list(filtered_books)
    print(allBooks)
    if allBooks:
        return HttpResponse(allBooks[0])
    return HttpResponse("No Book Found")

def books_home(request):
    return render(request , "books/home.html" ,
                  context={"name": "mohamed" , "books":books},
                  status=201)

def book_profile(request , id):
    filtered_books = filter(lambda book: book['id'] == id , books)
    filtered_books = list(filtered_books)
    if filtered_books:
        book = filtered_books[0]
        return render(request , "books/details.html", context ={
            "book": book
        })
    return HttpResponse("Book not Found")

def contact_us(request):
    return render(request , "books/contactUs.html" , status = 201)


def About(request):
    return render(request , "books/About.html" , status = 201)

def books_index(request):
    books = Book.objects.all()
    return render(request , "books/crud/index.html",
                  context={"books": books})


def book_show(request , id):
    # book = Book.objects.get(id=id)
    book = get_object_or_404(Book , pk=id)
    return render(request , "books/crud/show.html",
                  context = {"book":book})



def book_delete(request , id):
    book = get_object_or_404(Book , pk=id)
    book.delete()
    # return HttpResponse("book deleted")
    url = reverse("books.index")
    return redirect(url)

