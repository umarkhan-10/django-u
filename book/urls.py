from django.urls import path
from .views import book,authors

urlpatterns = [
    path('', book, name='book'),
    path('book/<int:book_id>/add-author/',authors, name='add_author'),

]