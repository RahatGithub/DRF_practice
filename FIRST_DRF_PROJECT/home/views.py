from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import *
from .serializers import *


class BooksAPI(APIView):

    def get(self, request):
        books_qs = Book.objects.all()
        serializer = BookSerializer(books_qs, many=True)
        return Response({
            'status' : 200,
            'payload' : serializer.data
        })

    def post(self, request):
        data = request.data 
        serializer = BookSerializer(data = request.data, many=True)

        if not serializer.is_valid():
            return Response({'status' : 403, 'message' : 'something went wrong!'})
        
        serializer.save()

        return Response({
            'status' : 201,
            'payload' : serializer.data,
            'message' : 'Your response is stored'
        })

    def delete(self, request):
        try:
            id = request.GET.get('id')
            book_obj = Book.objects.get(id=id)
            book_obj.delete()
            return Response({'status' : 200, 'message' : f'deleted successfulyy'})
        except Exception as e: 
            print(e)
            return Response({'status' : 403, 'message' : 'invalid id'})
        


@api_view(['GET'])
def search_book(request):
    author = request.GET.get('author')
    sort = request.GET.get('sort')
    order = request.GET.get('order')
    limit = request.GET.get('limit')

    try:
        books_qs = Book.objects.filter(author__icontains=author)
        if order and sort:
            if order == 'asc':
                books_qs = books_qs.order_by(sort)
            else:
                books_qs = books_qs.order_by(f'-{sort}')
        if limit:
            limit = int(limit)
            books_qs = books_qs[:limit]
        
        serializer = BookSerializer(books_qs, many=True)
        return Response({
            'status' : 200,
            'payload' : serializer.data
        })
    except Exception as e:
        print(e)
        return Response({'message': 'Something went wrong!'}, status=403)