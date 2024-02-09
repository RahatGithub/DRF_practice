from rest_framework import serializers 
from .models import *
from author_api.serializers import AuthorNameSerializer

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorNameSerializer(many=True, read_only=True)

    class Meta:
        app_label = 'book_api'
        model = Book
        fields = ['id', 'title', 'genre', 'price', 'publication', 'authors']
    
    # class Meta:
    #     app_label = 'book_api'
    #     model = Book 
    #     fields = '__all__'



