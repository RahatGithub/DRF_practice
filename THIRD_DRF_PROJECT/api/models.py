from django.db import models


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    dept = models.CharField(max_length=50)
    cgpa = models.FloatField()

    
class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    dept = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
