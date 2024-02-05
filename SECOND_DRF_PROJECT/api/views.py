from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import generics
from .models import Book
from .serializers import BookSerializer


class BookAPI(APIView):
    
    # serves FETCH ALL BOOKS and FETCH BOOK
    def get(self, request, **kwargs):
        if kwargs:
            id = kwargs.get('id')
            try:
                book = Book.objects.get(id=id)
                serializer = BookSerializer(book)
                return Response(serializer.data, status=200)
            except Book.DoesNotExist:
                return Response({"message": f"book with id: {id} was not found"}, status=404)
            
        else:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response({"books": serializer.data}, status=200)
    
    
    # serves POST BOOK
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data = data)
        
        if not serializer.is_valid():
            return Response({'status' : 403, 'message' : 'something went wrong!'})
        
        serializer.save()

        return Response(serializer.data, status=201)