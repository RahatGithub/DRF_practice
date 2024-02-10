from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .models import * 
from .serializers import *

class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer


class StationView(APIView):
    def get(self, request):
        queryset = Station.objects.all()
        serializer = StationSerializer(queryset, many=True)
        response_data = {"stations" : serializer.data}
        return Response(response_data, status=200) 


    def post(self, request):
        data = request.data
        serializer = StationSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"message" : "invalid request!"})


class StationTrainView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            station_id = kwargs.get('id')
            
            trains = Train.objects.all()
            stops = Stop.objects.all()

        except Exception as e:
            station_id = kwargs.get('id')
            message = f"station with id: {station_id} was not found"
            return Response({'message':message}, status=404)



class WalletView(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(user_id=id)
            response_data = {
                "wallet_id" : id,
                "balance" : user.balance,
                "wallet_user" : {
                    "user_id" : id,
                    "user_name" : user.user_name
                }
            } 
            return Response(response_data, status=200) 
        except User.DoesNotExist:
            message = {"message": f"wallet with id: {id} was not found"}
            return Response(message, status=404)
    
    def put(self, request, id):
        try:
            user = User.objects.get(user_id=id)
            recharge = request.data.get('recharge')
            new_balance = user.balance + recharge
            response_data = {
                "wallet_id" : id,
                "balance" : new_balance,
                "wallet_user" : {
                    "user_id" : id,
                    "user_name" : user.user_name
                }
            } 
            return Response(response_data, status=200) 
        except User.DoesNotExist:
            message = {"message": f"wallet with id: {id} was not found"}
            return Response(message, status=404)


class CreateTrainView(APIView):
    def post(self, request):
        input_data = request.data 
        stops = input_data.get("stops")
        station_ids = [stop.get("station_id") for stop in stops]
        data = {
            "train_id" : input_data.get('train_id'),
            "train_name" : input_data.get('train_name'),
            "capacity" : input_data.get('capacity'),
            "stops" : station_ids
        }

        for stop in stops:
            stop_data = {
                "station_id" : stop.get("station_id"),
                "arrival_time" : stop.get("arrival_time"),
                "departure_time" : stop.get("departure_time"),
                "fare" : stop.get("fare") 
            }
            stop_serializer = StopSerializer(data=stop_data)
            if stop_serializer.is_valid():
                stop_serializer.save()

        serializer = TrainSerializer(data = data)
        if serializer.is_valid():
            serializer.save() 
            response_data = {
                "train_id" : input_data.get('train_id'),
                "train_name" : input_data.get('train_name'),
                "capacity" : input_data.get('capacity'),
                "service_start" : stops[0].get("departure_time"),
                "service_ends" : stops[-1].get("arrival_time"),
                "num_stations" : len(stops)
            }
            return Response(response_data, status=201) # We need to fix response here!
        else:
            return Response({"message" : "invalid request!"})


class CreateTicketView(APIView):
    def post(self, request):
        try:
            pass 
        except Exception as e:
            pass
        