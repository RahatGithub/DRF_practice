from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True) 
    user_name = models.CharField(max_length=264)
    balance = models.IntegerField()
    def __str__(self):
        return self.user_name