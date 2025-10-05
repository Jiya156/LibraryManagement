from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from library.models import Book


def home(request):
    data = Book.objects.all()
    return render(request,"home.html",{"data":data})

def add(request):
    return render(request,"add.html")

def store(request):
    title = request.GET["title"]
    author = request.GET["author"]
    isbn = request.GET["isbn"]
    category = request.GET["category"]
    published_Year = request.GET["published_Year"]
    availability = request.GET.get("availability","False")
    availability = True if availability == "on" else False

    result = Book(title=title, author=author, isbn=isbn, 
    category=category, published_Year=published_Year, 
    availability=availability)
    result.save()

    return render(request,"added.html",{"msg":"Book added successfully"})

def delete(request,id):
    myid=id
    Book.objects.filter(id=myid).delete()
    return render(request,"delete.html")

def update(request,id):
    book = get_object_or_404(Book, id=id)
    return render(request,"updateform.html",{"book":book})

def submitupdate(request, id):
    book = get_object_or_404(Book, id=id)

    book.title = request.GET["title"]
    book.author = request.GET["author"]
    book.isbn = request.GET["isbn"]
    book.category = request.GET["category"]
    book.published_Year = request.GET["published_Year"]

    book.availability = request.GET.get("availability","False")
    book.availability = True if book.availability == "on" else False
    
    book.save()

    return render(request,"updated.html")