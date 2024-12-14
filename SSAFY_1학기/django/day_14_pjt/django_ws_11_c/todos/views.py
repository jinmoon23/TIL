from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer, TodoListSerializer, RecommendSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoListSerializer(todos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['DELETE','GET'])
def todo_detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    

@api_view(['POST'])
def recommend_create(request,todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        # 이거 정말 잘 까먹네.. data라는 키워드 인자를 명시해야 한다!!
        serializer = RecommendSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 기존에는 foreignKey 삽입 시 form.todo = todo 이런 방식이었음. 
            # 익숙해지자 어쩌겠어!
            serializer.save(todo=todo)
            return Response(serializer.data,status=status.HTTP_201_CREATED)