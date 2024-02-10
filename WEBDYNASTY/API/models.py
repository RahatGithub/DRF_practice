from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True) 
    user_name = models.CharField(max_length=264)
    balance = models.IntegerField()
    def __str__(self):
        return self.user_name
    

class Station(models.Model):
    station_id = models.IntegerField(primary_key=True) 
    station_name = models.CharField(max_length=264)
    longitude = models.FloatField()
    latitude = models.FloatField()
    def __str__(self):
        return self.station_name
    
    
class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key=True) 
    wallet_id = models.IntegerField()
    station_from = models.IntegerField()
    station_to = models.IntegerField()
 

class Stop(models.Model):
    station_id = models.IntegerField()
    arrival_time = models.CharField(max_length=5)  # Format: hh:mm
    departure_time = models.CharField(max_length=5)  # Format: hh:mm
    fare = models.IntegerField()


class Train(models.Model):
    train_id = models.IntegerField(primary_key=True)
    train_name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    stops = models.ManyToManyField(Stop, related_name='train_stops')
    def __str__(self):
        return self.train_name
