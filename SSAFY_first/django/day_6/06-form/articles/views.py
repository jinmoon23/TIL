from django.shortcuts import render, redirect
# 모델 클래스 가져오기
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # 게시글 전체 조회 요청 to DB
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # url로부터 전달받은 pk를 활용해 데이터를 조회
    # article = Article.objects.get(id=pk)
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 2. 유효성 검사
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # 아래가 기존의 new 로직이기 때문에 논리적으로 아래부터 작성하는것이 맞음
    else:
    # method가 POST가 아닐 때 
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html',context)

# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form
#     }
#     # 게시글 작성 페이지 응답
#     return render(request, 'articles/new.html',context)


# def create(request):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # 위 코드가 아래 코드로 단순화
#     # 1. 모델폼 인스턴스 생성(+ 사용자 입력 데이터를 통째로 인자로 작성)
#     form = ArticleForm(request.POST)
#     # article = Article(title=title, content=content)
#     # 2. 유효성 검사
#     if form.is_valid():
#         article = form.save()
#         return redirect('articles:detail', article.pk) 
#     context = {
#         'form' : form
#     }
#     return render(request,'articles/new.html',context)

def delete(request, pk):
    # 어떤 게시글 삭제할지 조회
    article = Article.objects.get(pk=pk)

    # 조회한 게시글 삭제
    article.delete()
    return redirect('articles:index')


# def edit(request, pk):
#     # 어떤 게시글을 수정할지 조회
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form
#     }
#     return render(request, 'articles/edit.html', context)


# def update(request, pk):
#     # 1. 어떤 게시글 수정할지 조회
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(request.POST,instance=article)
#     # 2. 유효성 검사
#     if form.is_valid():
#         form.save()
#         return redirect('articles:detail', article.pk)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request,'articles/edit.html',context)

def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=article)
        # 2. 유효성 검사
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form
    }    
    
    return render(request, 'articles/update.html', context)