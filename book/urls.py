from django.urls import path
from .views import book, authors, book_delete, author_detail

urlpatterns = [
    path('', book, name='book'),
    path('book/<int:book_id>/add-author/',authors, name='add_author'),
    path('book/delete/<int:id>/', book_delete, name='book_delete'),
    path('author/<int:id>/', author_detail, name='author_detail')

]