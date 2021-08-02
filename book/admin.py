from django.contrib import admin
from .models import Category, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'author', 'category']
    prepopulated_fields = {"slug": ("name",)}

    def book_name(self, obj):
        return f"{obj.name.upper()}"


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
