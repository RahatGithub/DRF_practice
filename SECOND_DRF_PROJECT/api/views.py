from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import generics
from .models import Book
from .serializers import BookSerializer, BookUpdateSerializer


class BookAPI(APIView):
    
    # serves FETCH ALL BOOKS and FETCH BOOK
    def get(self, request, id=None):
        
        searching = False  # by default, searching is False which means, any specific book is not being searched
        
        # checking the query parameters which may or may not exist
        title = request.GET.get('title')
        author = request.GET.get('author')
        genre = request.GET.get('genre')
        sort_field = request.GET.get('sort', 'id')
        order = request.GET.get('order', 'ASC')

        queryset = Book.objects.all()
        
        if title or author or genre:
            searching = True   
            if title:
                queryset = queryset.filter(title=title)
            elif author:
                queryset = queryset.filter(author=author)
            elif genre:
                queryset = queryset.filter(genre=genre)

        # Apply sorting
        if order == 'DESC':
            sort_field = '-' + sort_field

        # Sort the queryset
        queryset = queryset.order_by(sort_field)

        if id:
            try:
                book = Book.objects.get(id=id)
                serializer = BookSerializer(book)
                return Response(serializer.data, status=200)
            except Book.DoesNotExist:
                return Response({"message": f"book with id: {id} was not found"}, status=404)  
        else:
            if searching:
                books = [{
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'genre': book.genre,
                    'price': float(book.price)
                } for book in queryset]
                return Response({'books' : books}, status=200)
            
            else:
                # fetching all books
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
    

    # serves DELETE BOOKS
    def delete(self, request, id):
        book = Book.objects.get(id=id)
        book.delete() 
        return Response({"message" : f"deleted book with id: {id}"})
            