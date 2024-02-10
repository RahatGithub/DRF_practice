from rest_framework import serializers 
from .models import *

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'API'
        model = Station   
        fields = '__all__' 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'API'
        model = User   
        fields = '__all__' 


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'API'
        model = Train   
        fields = '__all__' 

class StopSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'API'
        model = Stop
        fields = '__all__' 