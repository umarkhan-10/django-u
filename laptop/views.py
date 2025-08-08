from django.shortcuts import render, HttpResponse,redirect
from laptop.models import Laptop


def laptop(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        generation = request.POST.get('generation')
        processor = request.POST.get('processor')
        ram = request.POST.get('ram')
        ssd = request.POST.get('ssd')
        detail = request.POST.get('detail')

        if name and image and generation and processor and ram and ssd and detail:
            laptop_obj = Laptop(
                name=name,
                image=image,
                generation=generation,
                processor=processor,
                ram=ram,
                ssd=ssd,
                detail=detail
            )
            laptop_obj.save()  

    return render(request, 'laptop.html')


def laptop_detail(request, id):
    laptop_detail = Laptop.objects.get(id=id)
    return render(request, 'laptop_detail.html', {'laptop_detail': laptop_detail})   

def laptop_edit(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')  # ✅ handles file uploads
        detail = request.POST.get('detail')
        Laptop.objects.filter(id=id).update(name=name, detail=detail)
        if image:
            laptop = Laptop.objects.get(id=id)
            laptop.image=image
            laptop.save()
        return redirect('laptop_detail', id=id)
    laptop=Laptop.objects.get(id=id)
    return render(request, 'laptop_edit.html',{'laptop': laptop})

def laptop_delete(request, id):
    Laptop.objects.get(id=id).delete()
    return redirect('about')