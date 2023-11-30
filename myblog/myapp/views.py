from django.shortcuts import render

from . models import Book, Publisher

# Create your views here.
def buku(request):
    data_buku = Book.objects.all()
    return render (request,'buku.html', {'data_buku':data_buku})

