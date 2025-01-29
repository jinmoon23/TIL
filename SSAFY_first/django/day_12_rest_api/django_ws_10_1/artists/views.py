from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArtistSerilizer
from .models import Artist
from rest_framework import status
# Create your views here.

@api_view(['GET','POST'])
def index(request):
    if request.method == 'POST':
        # 기존의 form 이었다면 위치인자에 대한 정의 없이
        # request.POST 이었을 텐데.. 다른점을 확인하자
        serializer = ArtistSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerilizer(artists,many=True)
        return Response(serializer.data)