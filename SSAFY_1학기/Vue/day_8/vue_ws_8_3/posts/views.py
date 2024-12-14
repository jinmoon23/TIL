from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PostsSerializer
from .models import Post
# Create your views here.
@api_view(['GET'])
def index(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        serializer = PostsSerializer(posts,many=True)
        return Response(serializer.data)