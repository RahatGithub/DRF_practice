from django.db import models


class Publication(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    starting_year = models.IntegerField()
    def __str__(self):
        return self.name 