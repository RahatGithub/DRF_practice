from rest_framework import serializers 
from .models import *

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'publication_api'
        model = Publication  
        fields = '__all__'