from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Todo
from .serializers import TodoSerializer


# Create your views here.
@api_view(['GET'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def todo_detail(request,id):
    todo = Todo.objects.get(pk=id)
    serializer = TodoSerializer(todo)
    return Response(serializer.data)