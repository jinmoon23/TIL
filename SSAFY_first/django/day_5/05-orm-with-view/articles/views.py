from django.shortcuts import render,redirect
# 모델 클래스 가져오기
from .models import Article

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request,pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    article = Article.objects.get(pk=pk)
    # article = Article.objects.get(id=pk)
    context = {
        'article' : article,
    }
    return render(request,'articles/detail.html',context)

def new(request):
    # 게시글 작성 페이지 응답
    return render(request,'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 1. 사용자 요청으로부터 입력 데이터를 추출
    # 2. 저장하기
    article = Article(title = title, content = content)
    # 3. 추출한 데이터를 활용해 데이터베이스에 저장 요청
    article.save()
    return redirect('articles:detail', article.pk)

def delete(request,pk):
    # 어떤 게시글을 삭제할지 조회(식별)
    article = Article.objects.get(pk=pk)
    # article = Article.objects.get(id=pk)
    article.delete()
    return redirect('articles:index')

def edit(request,pk):
    # 어떤 게시글을 삭제할지 조회(식별)
    article = Article.objects.get(pk=pk)
    # article = Article.objects.get(id=pk)
    context = {
        'article' : article
    }
    return render(request,'articles/edit.html',context)


def update(request, pk):
    # 1. 어떤 게시글 수정할지 조회
    article = Article.objects.get(pk=pk)
    # 2. 사용자로부터 받은 새로운 입력 데이터 추출
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 3. 기존 게시글의 데이터를 사용자에게서 받은 새로운 데이터로 재할당
    article.title = title
    article.content = content
    # 4. 저장
    article.save()
    return redirect("articles:detail", article.pk)