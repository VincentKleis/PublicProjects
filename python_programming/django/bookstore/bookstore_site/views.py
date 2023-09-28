from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bookstore(request):
    return render(request, 'bookstore.html', {})