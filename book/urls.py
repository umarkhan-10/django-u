from django.urls import path
from .views import book, book_delete

urlpatterns = [
    path('', book, name='book'),
    path('book/delete/<int:id>/', book_delete, name='book_delete'),

]