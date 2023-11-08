from django.shortcuts import render
from .models import Book

# Create your views here.
def book_store(request):
    book_title = Book.title
    #book_author = Book.author
    #book_pub_date = Book.pub_date
    #book_price = Book.price
    context = {
        'book_title':book_title,
        #'book_author':book_author,
        #'book_pub_date':book_pub_date,
        #'book_price':book_price,
    }
    return render(request, "books.html", context)