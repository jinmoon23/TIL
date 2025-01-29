from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import PostsSerializer, CategoriesSerializer, CommentSerializer
from .models import Post, Category, Comment

# Create your views here.
@api_view(['GET','POST'])
def postList_or_create(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        serializer = PostsSerializer(posts,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
def categoryList_or_create(request):
    categories = Category.objects.all()
    if request.method == 'GET':
        serializer = CategoriesSerializer(categories,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        

@api_view(['POST','GET'])
def comment(request,post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(post=post)
            return Response(status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        post_serializer = PostsSerializer(post)
        comments = Comment.objects.filter(post=post)
        comments_serializer = CommentSerializer(comments,many=True)
        data = {
            'post': post_serializer.data,
            'comments': comments_serializer.data
        }
        return Response(data)