from django.shortcuts import render
from .models import Nearby
from .serializers import Nearbyserializers
from rest_framework import generics
from rest_framework.response import Response

class Nearbycreateapi(generics.CreateAPIView):
    queryset = Nearby.objects.all()
    serializer_class = Nearbyserializers


class Nearbylistapi(generics.ListAPIView):
    queryset =  Nearby.objects.all()
    serializer_class = Nearbyserializers

class Nearbyupdateapi(generics.UpdateAPIView):
    queryset =  Nearby.objects.all()
    serializer_class = Nearbyserializers

class Nearbydeleteapi(generics.DestroyAPIView):
    queryset =  Nearby.objects.all()
    serializer_class = Nearbyserializers
