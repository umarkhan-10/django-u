from django.urls import path
from . import views

urlpatterns = [
    path("animes/", views.anime_list, name="anime_list"),
    path("author/<int:author_id>/", views.author_detail, name="author_detail"),
    path("anime/detail/<int:id>/", views.anime_detail, name="anime_detail")
]