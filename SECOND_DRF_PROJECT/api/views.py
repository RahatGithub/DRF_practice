from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, BookUpdateSerializer


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
    
    
    # serves ADD BOOKS
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"message" : "invalid request!"})
    

    # serves UPDATE BOOKS
    def put(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({"message": f"book with id: {id} was not found"}, status=404)

        serializer = BookUpdateSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()

            # adding 'id' to the response dictionary because the request body doesn't contain 'id' 
            result_dict = dict({'id' : int(id)})    
            additional_dict = dict(serializer.data) 
            result_dict.update(additional_dict)
            
            return Response(result_dict, status=200)
        return Response(serializer.errors, status=400)