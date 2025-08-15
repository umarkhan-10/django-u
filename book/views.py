from django.shortcuts import render, get_object_or_404, redirect
from book.models import Book,Authors
from django.utils import timezone

def book(request):
    if request.method=="POST":
        title = request.POST['title']
        image = request.FILES.get('image')
        author_id = request.POST['author']
        author = Authors.objects.get(id=author_id)
        publishyear = request.POST['publishyear']
        book = Book(title=title, image=image, author=author, publishyear=publishyear)
        book .save()
        return redirect("book")
    authors = Authors.objects.all()
    return render(request, "book_form.html",{"authors":authors})
    
def authors(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        name = request.POST['name']
        image = request.FILES.get('image')
        dateofbirth = request.POST['dateofbirth']
        publishedbooks = request.POST['publishedbooks']

        author = Authors(
            name=name,
            image=image,
            dateofbirth=dateofbirth,
            publishedbooks=publishedbooks,
            book=book  # connect author to this book
        )
        author.save()

def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books')        