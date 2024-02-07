from django.db import models


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6)
    def __str__(self):
        return self.name 