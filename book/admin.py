from django.contrib import admin
from .models import Book, Authors, Country

admin.site.register(Book)
admin.site.register(Authors)
admin.site.register(Country)