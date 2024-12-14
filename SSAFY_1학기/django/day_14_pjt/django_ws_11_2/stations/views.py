from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import StationListSerializers,LocationListSerializers,StationSerializers
from .models import Station,Location
# Create your views here.
@api_view(['GET','POST'])
def station_list(request):
    if request.method == 'GET':
        stations = Station.objects.all()
        serializer = StationListSerializers(stations,many=True)
        return Response(serializer.data)

@api_view(['POST','GET'])
def station(request,location_pk):
    location = Location.objects.get(pk=location_pk)
    if request.method == 'POST':
        serializer = StationSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(address=location)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        serializer = StationSerializers(location)
        return Response(serializer.data)
    
@api_view(['GET'])
def station_detail(request,station_pk):
    station = Station.objects.get(pk=station_pk)
    if request.method == 'GET':
        serializer = StationSerializers(station)
        return Response(serializer.data)

@api_view(['GET','POST'])
def location_list(request):
    if request.method == 'POST':
        serializer = LocationListSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        locations = Location.objects.all()
        serializer = LocationListSerializers(locations,many=True)
        return Response(serializer.data)