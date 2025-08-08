from django.urls import path
from .views import game_detail,game,game_edit,game_delete

urlpatterns = [
    path('', game, name='game'),
    path('game/<int:id>/', game_detail, name='game_detail'),
    
    path('game/edit/<int:id>/', game_edit, name='game_edit'),
    path('game/delete/<int:id>/', game_delete, name='game_delete'),
]