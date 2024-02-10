from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import * 
from .serializers import StationSerializer


class StationListView(ListAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


# class StationTrainsView(APIView):
#     def get(self, request, station_id):
#         try:
#             # Retrieve the station object by station_id
#             station = Station.objects.get(station_id=station_id)
            
#             # Retrieve all trains passing through the station
#             trains = []
#             for stop in station.stop_set.all():
#                 train_info = {
#                     "train_id": stop.train.train_id,
#                     "arrival_time": stop.arrival_time,
#                     "departure_time": stop.departure_time
#                 }
#                 trains.append(train_info)
            
#             # Prepare the response data
#             response_data = {
#                 "station_id": station.station_id,
#                 "trains": trains
#             }
            
#             # Return the response with a 200 status code
#             return Response(response_data, status=200)
        
#         except Station.DoesNotExist:
#             # If the station with the given ID does not exist, return a 404 response
#             message = {"message": f"station with id: {station_id} was not found"}
#             return Response(message, status=404)