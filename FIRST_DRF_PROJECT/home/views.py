from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *


@api_view(['GET', 'POST'])
def home(request):
    
    if request.method == 'POST': 
        data = request.data 
        serializer = BookSerializer(data = request.data)
        return Response({
            'status' : 201,
            'payload' : data,
            'message' : 'Your response is stored'
        })

    else:   # 'GET' request
        books_qs = Book.objects.all()
        serializer = BookSerializer(books_qs, many=True)
        return Response({
            'status' : 200,
            'payload' : serializer.data
        })