from django.shortcuts import render
from .models import Book

# Create your views here.
def book_list(request):
    book = Book.objects.all()
    print(book)

    context = {
        'books':book
    }
    return render(request, "bookstore.html", context)