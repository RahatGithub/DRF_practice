from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
# from django.core.serializers import serialize
import json
from rest_framework.views import APIView
from django.db.models import Q
from .models import *
from .serializers import *


class BooksAPI(APIView):
    
    def get(self, request, id=None):
        # Extract query parameters
        title = request.GET.get('title')
        author = request.GET.get('author')
        genre = request.GET.get('genre')
        sort_field = request.GET.get('sort', 'id')
        order = request.GET.get('order', 'ASC')

        queryset = Book.objects.all()
        no_searching = False 
        if not title and not author and not genre:
            no_searching = True 
        
        if title:
            queryset = queryset.filter(title__icontains=title)
        if author:
            queryset = queryset.filter(author__icontains=author)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)

        # Apply sorting
        if order == 'DESC':
            sort_field = '-' + sort_field

        # Sort the queryset
        queryset = queryset.order_by(sort_field)

        if id is not None:
            try:
                book = Book.objects.get(id=id)
                serializer = BookSerializer(book)
                return Response(serializer.data, status=200)
            except Book.DoesNotExist:
                return Response({"message": f"book with id: {id} was not found"}, status=404)
        else:
            if no_searching:
                # nothing is being searched
                books = Book.objects.all()
                serializer = BookSerializer(books, many=True)
                return Response({'books': serializer.data}, status=200)
            else: 
                books = [{
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'genre': book.genre,
                    'price': float(book.price)
                } for book in queryset]
                # Return the response
                return Response({'books': books})


    def post(self, request):
        data = request.data
        serializer = BookSerializer(data = data)
        
        if not serializer.is_valid():
            return Response({'status' : 403, 'message' : 'something went wrong!'})
        
        serializer.save()

        return Response(serializer.data, status=201)


    def put(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response({"message": f"book with id: {id} was not found"}, status=404)

        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

        

# @api_view(['GET'])
# def search_book(request):
#     # Extract query parameters
#     title = request.GET.get('title')
#     author = request.GET.get('author')
#     genre = request.GET.get('genre')
#     sort_field = request.GET.get('sort', 'id')
#     order = request.GET.get('order', 'ASC')

#     # Construct the base queryset
#     queryset = Book.objects.all()

#     # Apply search filters if provided
#     if title:
#         queryset = queryset.filter(title__icontains=title)
#     if author:
#         queryset = queryset.filter(author__icontains=author)
#     if genre:
#         queryset = queryset.filter(genre__icontains=genre)

#     # Apply sorting
#     if order == 'DESC':
#         sort_field = '-' + sort_field

#     # Sort the queryset
#     queryset = queryset.order_by(sort_field)

#     if not title and not author and not genre:
#         queryset = Book.objects.all()

#     # Serialize the queryset into JSON format
#     books = [{
#         'id': book.id,
#         'title': book.title,
#         'author': book.author,
#         'genre': book.genre,
#         'price': float(book.price)
#     } for book in queryset]

#     # Return the response
#     return Response({'books': books})