from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import * 


class WalletView(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
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
            message = {"message": f"station with id: {id} was not found"}
            return Response(message, status=404)