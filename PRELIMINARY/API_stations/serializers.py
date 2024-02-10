from rest_framework import serializers 
from .models import *

class StationSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'API_stations'
        model = Station   
        fields = '__all__' 


# class TrainSerializer(serializers.ModelSerializer):
#     class Meta:
#         app_label = 'API_stations'
#         model = Train 
#         fields = '__all__' 


# class StopSerializer(serializers.ModelSerializer):
#     class Meta:
#         app_label = 'API_stations'
#         model = Stop 
#         fields = '__all__' 