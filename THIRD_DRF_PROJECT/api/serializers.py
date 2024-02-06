from rest_framework import serializers 
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'api'
        model = Student  
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        app_label = 'api'
        model = Teacher   
        fields = '__all__'