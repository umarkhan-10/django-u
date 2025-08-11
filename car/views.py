from django.shortcuts import render , HttpResponse, redirect, get_object_or_404
from car.models import Car, Review
from django.utils import timezone


def car(request):
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES.get('image')
        model = request.POST['model']
        engine = request.POST['engine']
        enginepower = request.POST['enginepower']
        price = request.POST['price']
        madein = request.POST['madein']
        topspeed = request.POST['topspeed']
        car = Car(name=name, image=image, model=model, engine=engine, enginepower=enginepower, price=price, madein=madein, topspeed=topspeed)
        car.save()
    return render(request, "car_form.html")

def car_list(request):
    cars = Car.objects.all().order_by('-timeStamp')
    return render(request, 'cars.html', {'car': cars})

def car_review(request, id):
    car = get_object_or_404(Car, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        review_text = request.POST.get('review')
        rating = request.POST.get('rating')
        created_at=timezone.now()

        # convert rating to int safely
        try:
            rating = int(rating)
        except (TypeError, ValueError):
            rating = 0

        Review.objects.create(
            car=car,
            name=name,
            review=review_text,
            rating=rating,
        )
        return redirect('car_detail', id=car.id)

    return render(request, 'review.html', {'car': car})

def car_detail(request, id):
    car_detail = get_object_or_404(Car, id=id)
    reviews = car_detail.reviews.all().order_by('-created_at')  # fetch related reviews
    return render(request, 'car_detail.html', {
        'car_detail': car_detail,
        'reviews': reviews
    })

def car_edit(request, id):
    car = get_object_or_404(Car, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        model = request.POST.get('model')
        engine = request.POST.get('engine')
        enginepower = request.POST.get('enginepower')
        price = request.POST.get('price')
        madein = request.POST['madein']
        topspeed = request.POST['topspeed']

        if not name or not model or not engine or not enginepower or not price or not madein or not topspeed:
            return render(request, 'car_edit.html', {
                'car': car,
                'error': 'Please fill in all fields.'
            })

        car.name = name
        car.model = model
        car.engine = engine
        car.enginepower = enginepower
        car.price = price
        car.madein = madein
        car.topspeed = topspeed

        if image:
            car.image = image

        car.save()
        return redirect('car_detail', id=car.id)

    return render(request, 'car_edit.html', {'car': car})

def car_delete(request, id):
    car = get_object_or_404(Car, id=id)
    car.delete()
    return redirect('car_home')