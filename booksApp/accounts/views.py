from django.shortcuts import render , redirect , reverse


# Create your views here.

def profile_view(request):
    url = reverse("books.index")
    return redirect(url)

