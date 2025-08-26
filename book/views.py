from django.shortcuts import render, get_object_or_404, redirect
from book.models import Book 
from django.utils import timezone

def book(request):
    if request.method=="POST":
        title = request.POST['title']
        image = request.FILES.get('image')
        publishyear = request.POST['publishyear']
        book = Book(title=title, image=image, publishyear=publishyear)
        book .save()
        return redirect("book")

    return render(request, "book_form.html")

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books')          