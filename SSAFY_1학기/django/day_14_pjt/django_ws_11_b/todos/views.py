from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer

# Create your views here.
@api_view(['GET','POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        # 1. 유효성 검사 / raise_exception를 통해 유효성 검사를 통과하지 못한 경우의 status code 대응
        if serializer.is_valid(raise_exception=True):
            # 2. 저장
            serializer.save()
            # 3. return
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE'])
def todo_detail(request,todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
