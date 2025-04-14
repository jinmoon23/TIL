from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)

def new_todo(request):
    work = request.POST.get('work')
    content = request.POST.get('content')
    is_completed = False

    todo = Todo(work=work, content=content, is_completed=is_completed)
    todo.save()
    return redirect('todos:detail', todo.pk)

def delete_todo(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')

def edit(request,todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    work = todo.work
    content = todo.content
    pk = todo.pk

    context = {
        'work' : work,
        'content': content,
        'pk' : pk,
    }
    return render(request, 'todos/edit.html',context)

def update(request,todo_pk):
    # 1. 식별
    todo = Todo.objects.get(pk=todo_pk)
    # 2. 수정사항으로 입력 받은 데이터를 받아옴
    work = request.POST.get('work')
    content = request.POST.get('content')
    # 3. 기존의 데이터를 수정 사항으로 재할당
    todo.work = work
    todo.content = content
    # 4. 저장
    todo.save()
    return redirect('todos:detail', todo.pk)
    