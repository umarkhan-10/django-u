from django.contrib import admin
from .models import Book, Authors

admin.site.register(Book)
admin.site.register(Authors)