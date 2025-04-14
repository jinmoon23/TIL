from django.shortcuts import render
from .models import Todo
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }
    return render(request, 'todos/index.html', context)

def create(request):
    return render(request, 'todos/create.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)