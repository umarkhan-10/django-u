from django.http import HttpResponse
from django.shortcuts import render
from games.models import Games
from laptop.models import Laptop
from car.models import Car


def index(request):
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