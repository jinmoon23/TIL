from django.shortcuts import render
from .forms import MyAppForm

# Create your views here.
def index(request):
    return render(request,'my_app/index.html')

def create(request):
    if request.method == 'POST':
        pass
    else:
        form = MyAppForm
    context = {
        'form': form,
    }
    return render(request,'my_app/create',context)