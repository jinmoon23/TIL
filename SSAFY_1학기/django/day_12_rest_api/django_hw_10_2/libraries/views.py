from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book

# Create your views here.
@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def detail(request,book_pk):
    if request.method == 'GET':
        book = Book.objects.get(pk=book_pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)