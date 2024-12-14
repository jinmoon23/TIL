from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Artist
from .serializers import ArtistSerializer


# Create your views here.
@api_view(['GET','POST'])
def artist_list_or_create(request):
    if request.method == 'POST':
        serializer = ArtistSerializer(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        # 1. 조회하고자 하는 쿼리셋 파악
        artists = Artist.objects.all()
        # 2. serializaion 진행
        serializer = ArtistSerializer(artists,many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def detail(request,artist_pk):
    if request.method == 'GET':
        artist = Artist.objects.get(pk=artist_pk)
        serializer = ArtistSerializer(artist)
        return Response(serializer.data,status=status.HTTP_200_OK)