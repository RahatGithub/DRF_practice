from rest_framework import serializers 
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'book_api'
        model = Book 
        fields = '__all__'