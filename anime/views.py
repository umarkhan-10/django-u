from django.shortcuts import render , HttpResponse, redirect, get_object_or_404
from .models import Anime, Author


# Create your views here.
def anime_list(request):
    animes = Anime.objects.all()   # Database se sab animes nikal li
    return render(request, "animes.html", {"animes": animes})


def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    animes = Anime.objects.filter(author=author)  # is author ke sab anime lao
    return render(request, "author_detail.html", {"author": author, "animes": animes})


def anime_detail(request, id):
    anime_detail = get_object_or_404(Anime, id=id)

    return render(request, 'anime_detail.html', {
        'anime_detail': anime_detail,
    })
