from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import * 
from .serializers import *


# handling APIs related to students
class StudentAPI(APIView):
    
    def get(self, request, id=None):
        if id:
            try:
                student = Student.objects.get(id=id)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=200)
            except Student.DoesNotExist:
                return Response({"message" : f"student with id: {id} not found"})
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response({"students" : serializer.data}, status=200)
    

    def post(self, request):
        result = create_instance(request, Student)
        return Response(result, status=201)
    

    def put(self, request, id):
        return update_instance(request, Student, id) 


    def patch(self, request, id):
        return update_instance(request, Student, id)


    def delete(self, request, id):
        response = destroy_instance(request, Student, id)
        return Response({"message" : response}, status=200)

    



# handling APIs related to teachers
class TeacherAPI(APIView):

    def get(self, request, id=None):
        if id:
            try:
                teacher = Teacher.objects.get(id=id)
                serializer = TeacherSerializer(teacher)
                return Response(serializer.data, status=200)
            except Teacher.DoesNotExist:
                return Response({"message" : f"teacher with id: {id} not found"})
        else:
            teachers = Teacher.objects.all()
            serializer = TeacherSerializer(teachers, many=True)
            return Response({"teachers" : serializer.data}, status=200)
    

    def post(self, request):
        response = create_instance(request, Teacher)
        return Response(response, status=201)


    def put(self, request, id):
        return update_instance(request, Teacher, id) 


    def patch(self, request, id):
        return update_instance(request, Teacher, id) 


    def delete(self, request, id):
        response = destroy_instance(request, Teacher, id)
        return Response({"message" : response}, status=200)



# ************* SUPPORTIVE FUNCTIONS ****************

def create_instance(request, model):
    model_name = model.__name__  # it will return the model's name (e.g. Student, Teacher)
    if model_name == 'Student':
        serializer = StudentSerializer(data = request.data)
    elif model_name == 'Teacher':
        serializer = TeacherSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    return serializer.data


def update_instance(request, model, id):
    model_name = model.__name__
    try:
        instance = model.objects.get(id=id)
    except model.DoesNotExist:
        return Response({"message": f"{model_name} with id: {id} was not found"}, status=404)

    partial = True # by default we're assuming it's a PATCH request
    if request.method == 'PUT': 
        partial = False
    
    if model_name == 'Student':
        serializer = StudentSerializer(instance, data=request.data, partial=partial)
    elif model_name == 'Teacher':
        serializer = TeacherSerializer(instance, data=request.data, partial=partial)

    if serializer.is_valid():
        serializer.save()
        result = generate_full_dict(id, serializer.data)
        return Response(result, status=200)
    return Response(serializer.error, status=400)


def destroy_instance(request, model, id):
    model_name = model._meta.model_name # it will return the model's name in lowercase (e.g. student, teacher)
    try:
        instance = model.objects.get(id=id)
        instance.delete()
        return f"deleted {model_name} with id: {id}"
    except Exception as e:
        return f"{model_name} with id: {id} was not found"


# generates a dull dictionary of the object to return because bodies of PUT and PATCH requests don't contain the full object
def generate_full_dict(id, serializer_data):
        result_dict = dict({'id' : int(id)})
        additional_dict = dict(serializer_data)
        result_dict.update(additional_dict)
        return result_dict