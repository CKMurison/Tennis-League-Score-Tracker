from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response

class ReactView(APIView):
    def get(self, request):
        players = Player.objects.all()
        serializer = ReactSerializer(players, many=True)  
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReactSerializer (data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save ()
            return Response(serializer .data)
