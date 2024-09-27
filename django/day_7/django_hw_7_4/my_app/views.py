from django.shortcuts import render,redirect
from .forms import MyAppForm
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles,
    }
    return render(request,'my_app/index.html',context)

def create(request):
    if request.method == 'POST':
        form = MyAppForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()
            return redirect('my_app:index')
    else:
        form = MyAppForm
    context = {
        'form': form,
    }
    return render(request,'my_app/create.html',context)