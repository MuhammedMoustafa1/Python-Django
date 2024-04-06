from django import forms
from books.models import Book

class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 3:
            raise forms.ValidationError('Title length must be greater then 3 characters')
        return title

    def clean_price(self):
        price = self.cleaned_data['price']
        if price is not None and price < 20 :
            raise forms.ValidationError('Price should be greater than 20$')
        return price

    def clean_num_of_pages(self):
        pages = self.cleaned_data['num_of_pages']
        if pages is not None and pages < 10:
            raise forms.ValidationError('Number of pages should be greater than 10')
        return pages

    def clean_author(self):
        author = self.cleaned_data['author']
        if len(author) < 3:
            raise forms.ValidationError('Author length must be greater than 3 characters')
        return author
