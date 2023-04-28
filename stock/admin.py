from django.contrib import admin
from .models import Item, Author, Comment, Post

# Register your models here.

myModels = [Item, Author, Comment, Post]
admin.site.register(myModels)