from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html',context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html',context)

def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST,instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)

# def delete(request, article_pk):
#     return redirect('articles:index')

def comment_create(request, article_pk):
    # 1. 어떤 article의 댓글이야?
    article = Article.objects.get(pk=article_pk)
    # 2. 받아온 comment 유효성 검사 실시해!
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 3. 바로 save()하면 db 무결성 오류가 발생함!
        # 이유는 foreignKey 값을 설정해주지 않았기 때문
        # 저장을 유예하고 객체를 반환하는 commit 인자를 활용
        comment = comment_form.save(commit=False)
        # 아래 코드로 무결성 오류 배제
        comment.article = article
        # 비로소 저장 성공!
        comment.save() 
    return redirect('articles:detail', article_pk)

# def comment_delete(request, article_pk):
#     return redirect('articles:detail', article_pk)
