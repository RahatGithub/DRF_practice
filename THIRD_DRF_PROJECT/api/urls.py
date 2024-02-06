from django.urls import path
from .views import *

urlpatterns = [
    
    # endpoints related to students
    path('students', StudentAPI.as_view()),
    path('students/<int:id>', StudentAPI.as_view()),

    # endpoints related to teachers
    path('teachers', TeacherAPI.as_view()),
    path('teachers/<int:id>', TeacherAPI.as_view())
]
