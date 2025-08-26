from django.http import HttpResponse
from django.shortcuts import render
from games.models import Games
from laptop.models import Laptop
from car.models import Car
from book.models import Book


def index(request):
    car = Car.objects.first()  # or get a specific car
    return render(request,'index.html')

def car_home(request):
    cars = Car.objects.all()
    context = {
        "cars": cars
    }
    return render(request,'car_home.html', context)    

def home(request):
    games = Games.objects.all()
    context = {
        "games": games
    }
    return render(request, 'home.html', context)
    
def about(request):
    laptops = Laptop.objects.all()
    context = {
        "laptops": laptops
    }
    return render(request, 'about.html', context)

def books_view(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, 'books.html', context)

def animes_view(request):
    from anime.models import Anime
    animes = Anime.objects.all()
    return render(request, "animes.html", {"animes": animes})
    



