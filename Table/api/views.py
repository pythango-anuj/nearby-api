# Using generic class
'''
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
'''

# Using APIview
from .models import Nearby
from .serializers import Nearbyserializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

class NearbyapiList(APIView):
    def get(self,request,format = None):
        queries = Nearby.objects.all()
        serializer = Nearbyserializers(queries,many = True)
        return Response(serializer.data)

    def post(self,request,format = None):
        serializer = Nearbyserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class NearbyapiDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Nearby.objects.get(pk=pk)
        except Nearby.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        query = self.get_object(pk)
        serializer = Nearbyserializers(query)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        query = self.get_object(pk)
        serializer = Nearbyserializers(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        query = self.get_object(pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)