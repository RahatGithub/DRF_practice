from django.db import models
from author_api.models import Author 
from publication_api.models import Publication


class Book(models.Model):
    id = models.IntegerField(primary_key=True) 
    title = models.CharField(max_length=264)
    authors = models.ManyToManyField(Author)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
    genre = models.CharField(max_length=264, blank=True) 
    price = models.FloatField(blank=True)
    def __str__(self):
        return self.title 