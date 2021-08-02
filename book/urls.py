from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/add', views.book_add, name='book_add'),
    path('books/edit/<str:book_slug>', views.book_edit, name='book_edit'),
    path('books/delete/<int:pk>', views.book_delete, name='book_delete'),
    path('books/<str:slug>', views.book_detail, name='book_detail'),
]