from django.shortcuts import render,redirect
from games.models import Games
from django.shortcuts import render

def game(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')  # ✅ handles file uploads
        message = request.POST.get('message')
        if name and image and message:  # optional: basic validation
            games_obj = Games(name=name, image=image, message=message)
            games_obj.save()
    return render(request, 'game.html')


def game_detail(request, id):
    game_detail = Games.objects.get(id=id)
    return render(request, 'game_detail.html', {'game_detail': game_detail})


def game_edit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')  # ✅ handles file uploads
        message = request.POST.get('message')
        Games.objects.filter(id=id).update(name=name, message=message)
        if image:
            game = Games.objects.get(id=id)
            game.image=image
            game.save()
        return redirect('game_detail', id=id)
    game=Games.objects.get(id=id)
    return render(request, 'game_edit.html',{'game': game})

def game_delete(request, id):
    Games.objects.get(id=id).delete()
    return redirect('home')
