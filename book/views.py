from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .models import Book
from .forms import AddNewBookForm

# CRUD operations.
# Retrieve / get data.
# get book list.
def book_list(request):
    books = Book.objects.all()
    search_query = request.GET.get('q')
    if search_query:
        books = books.filter(
            Q(name__icontains=search_query) |
            Q(author__username__icontains=search_query)
        )

    context = {"books": books, 'name': 'sdfasfasdf'}
    print(books, search_query)
    return render(request, 'book/book_list.html', context=context)

# get specific book (by pk/slug...)
def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'book/book_detail.html', context={'book': book})

# add new book
def book_add(request):
    form = AddNewBookForm()
    if request.method == "POST":
        form = AddNewBookForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.slug = slugify(instance.name)
            instance.save()
            messages.success(request, 'Book added successfully')
            
        return redirect('book:book_list')
    return render(request, 'book/add_book.html', context={'form': form})

# book edit.
def book_edit(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    form = AddNewBookForm(instance=book)
    if request.method == 'POST':
        form = AddNewBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book edited successfully')
            return redirect('book:book_detail', slug=book_slug)
    return render(request, 'book/add_book.html', {'form': form})

def book_delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('book:book_list')