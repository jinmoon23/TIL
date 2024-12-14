from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import CreateAuthorform, CreateNovelForm
from django.contrib.auth import get_user
# Create your views here.
def index(request):
    return render(request, 'libraries/index.html')

def novels(request):
    books = Book.objects.all()
    context = {
        'books':books,
    }
    return render(request,'libraries/novels.html',context)

def create_author(request):
    if request.method == 'POST':
        form = CreateAuthorform(request.POST)
        if form.is_valid():
            # 1. user foreignKey를 설정하기 위해 save 보류
            author = form.save(commit=False)
            # 2. user를 변수에 담기
            user = request.user
            # 3. user 값 설정
            author.user = user
            # 4. save
            author.save()
            return redirect('accounts:my_profile')
    else:
        form = CreateAuthorform()    
    context = {
        'form': form,
    }
    return render(request,'libraries/create_author.html',context)

def create_novel(request):
    if request.method == 'POST':
        form = CreateNovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libraries:novels')
    else:
        form = CreateNovelForm()
    context = {
        'form': form,
    }
    return render(request,'libraries/create_novel.html',context)