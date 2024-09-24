from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    # work = request.GET.get('work')
    todo_list = Todo.objects.all()
    context = {
        # 'work': work
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def new(request):
    todo = Todo()
    todo.work = request.POST.get('work')
    todo.content = request.POST.get('content')
    todo.is_completed = False
    todo.save()
    return redirect('todos:detail',todo.pk)

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def delete(request,todo_pk):
    # 1. 식별
    todo = Todo.objects.get(pk=todo_pk)
    # 2. 삭제 및 상태저장
    todo.delete()
    return redirect('todos:index')