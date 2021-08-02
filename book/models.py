from django.contrib.auth.models import User
from django.db import models

def upload_img(instance, filename):
    extension = filename.split(".")[-1]
    renamed = f"{instance.name}.{extension}"
    return F"books/img/{renamed}"

def upload_files(instance, filename):
    extension = filename.split(".")[-1]
    renamed = f"{instance.name}.{extension}"
    return F"books/file/{renamed}"

# Category.
class Category(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title

# Book.
class Book(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    img = models.ImageField(blank=True, null=True, upload_to=upload_img)
    file = models.FileField(blank=True, null=True, upload_to=upload_files)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rate = models.DecimalField(max_digits=4, decimal_places=2)
    
    def __str__(self):
        return self.name
