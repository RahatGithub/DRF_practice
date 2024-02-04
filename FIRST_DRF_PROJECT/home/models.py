from django.db import models


class Book(models.Model):
    id = models.IntegerField(primary_key=True) 
    title = models.CharField(max_length=264)
    author = models.CharField(max_length=264) 
    genre = models.CharField(max_length=264, blank=True) 
    price = models.FloatField(blank=True)

    def __str__(self):
        return self.title 

