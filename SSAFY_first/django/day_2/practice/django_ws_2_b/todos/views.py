from django.shortcuts import render

# Create your views here.
todo_list = []
def index(request):
    work = request.GET.get('work')
    if work:
        todo_list.append(work)
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html',context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')