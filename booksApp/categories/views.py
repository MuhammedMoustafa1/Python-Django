from django.shortcuts import render , reverse , redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from categories.forms import CategoryModelForm
from categories.models import Category


# Create your views here.
@login_required
def create_category(request):
    form = CategoryModelForm()
    if request.method == "POST":
        form = CategoryModelForm(request.POST , request.FILES)
        if form.is_valid():
            category = form.save()
            url = reverse("categories.index")
            return redirect(url)

    return render(request , 'categories/create.html',
                  {'form': form})

@login_required
def categories_index(request):
    categories = Category.get_all_categories()
    return render(request , 'categories/index.html' , {'categories': categories})
@login_required
def category_delete(request , id):
    category = get_object_or_404(Category , pk=id)
    category.delete()
    url = reverse("categories.index")
    return redirect(url)
@login_required
def category_show(request  , id):
    category = get_object_or_404(Category , pk = id)
    return render(request , "categories/show.html" , context = {"category": category})
@login_required
def edit_category(request  ,id):
    category = Category.get_category_by_id(id)
    form  = CategoryModelForm(instance = category)
    if request.method == "POST":
        form = CategoryModelForm(request.POST , request.FILES,instance=category)
        if form.is_valid():
            category = form.save()
            return redirect(category.show_url)

    return render(request , 'categories/edit.html',
                  context={"form": form})
