from django import forms
from .models import Book

class AddNewBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'img', 'file', 'category', 'price', 'rate']

