from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    print(request.user.is_authenticated)
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            # 현재 로그인 중인 유저가 요청한 것이란 것을 어떻게 저장할 수 있을까??
            # 즉, user foreignKey를 설정할 수 있어야 한다.
            # user의 경우 특별한 방법이 있..던가?
            
            # 1. 최종 저장을 유예한다!
            todo = form.save(commit=False)
            # 2. 요청을 한 유저의 정보를 request.user를 통해 식별하고 
            # 그 유저 정보를 foreignKey에 저장한다.
            todo.user = request.user
            # 3. 최종 저장 진행시켜~
            todo.save()
            # 결국 기존과 다른 부분은 요청한 유저의 정보를 request에서 받아온 다는 점 뿐!
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm()
    context = {
        'form': form
    }
    return render(request, 'todos/create.html', context)
    
def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('todos:index')
    else:
        return redirect('todos:detail', todo.pk)

def update(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form': form
    }
    return render(request, 'todos/update.html', context)