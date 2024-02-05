from rest_framework import serializers 
from .models import *

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'api'
        model = Book 
        fields = '__all__'
        