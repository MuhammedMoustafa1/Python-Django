from django.urls import path
from categories.views import create_category , categories_index , category_delete , category_show,edit_category

urlpatterns = [
    path('create', create_category , name='categories.create'),
    path('', categories_index , name = 'categories.index'),
    path('<int:id>/delete' ,category_delete , name = 'categories.delete'),
    path('<int:id>' , category_show , name = "categories.show"),
    path('<int:id>/edit' , edit_category , name= "categories.edit")
]