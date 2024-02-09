from rest_framework import serializers 
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'author_api'
        model = Author  
        fields = '__all__' 


class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'author_api'
        model = Author  
        fields = ['name']