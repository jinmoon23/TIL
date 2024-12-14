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
        # 1. 직렬화(serialization), 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를
        # 나중에 재구성할 수 있는 포맷으로 변환하는 과정
        # many 인자는 serialize 대상이 쿼리셋인 경우 필수인자
        # todos는 쿼리셋이기 때문에(all()) 이 경우 반드시 작성해야 한다.
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)