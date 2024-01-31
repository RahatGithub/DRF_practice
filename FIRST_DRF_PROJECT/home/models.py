from django.db import models


class Book(models.Model):
    id = models.AutoField(primary_key=True) 
    title = models.CharField(max_length=264)
    author = models.CharField(max_length=264) 
    price = models.FloatField(blank=True)

    def __str__(self):
        return self.title 

