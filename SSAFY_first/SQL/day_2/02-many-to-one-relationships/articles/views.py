from django.shortcuts import render, redirect
# 인증 관련 데코레이터
from django.contrib.auth.decorators import login_required
# HTTP를 위한 데코레이터
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article, Comment 
from .forms import ArticleForm, CommentForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# article의 detail 페이지에서는 pk 값을 라우팅 받기 때문에
# pk에 대한 접근이 가능하고 이를 활용할 수 있다.
@login_required
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 해당 게시글에 작성된 모든 댓글 조회
    comments = article.comment_set.all()
    context = {
        'article': article,
        'form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)

def comment_create(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 외래키를 넣어야 함
        # 1. comment 인스턴스 필요
        # 2. save() 메서드가 호출되기 전이어야 함
        # 그런데 1은 2가 완료되어야 생성됨
        # 해결방법: save 메서드는 인스턴스만 제공하고 실제 저장은 대기하는 인자 존재
        # save(commit=False) 
        comment = comment_form.save(commit=False)
        # 외래키를 포함한 article
        comment.article = article
        # 댓글에 작성자 정보 추가하기
        comment.user = request.user
        comment.save()
        return redirect('articles:detail',pk)
    context = {
        'article':article,
        'form':comment_form,
    }
    return render(request,'articles/detail',context)

def comment_delete(request,article_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # 첫번째 방법
    # article_pk = comment.article.pk
    # 권한이 있는 유저만 삭제할 수 있도록 분기처리
    if request.user == comment.user:
        comment.delete()
    # 삭제되는 댓글의 게시글 pk가 필요하다!
    # 두번째 방법
    return redirect('articles:detail',article_pk)

@login_required
@require_http_methods(['POST','GET'])
def create(request):
    if request.method == 'POST':
        # 사용자가 넘겨준 데이터에 user 정보는 없다.
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            # 유저 요청(request)에 해당하는 유저의 정보가 담겨있다.
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

# 업데이트는 수정할 거 없음 ^_^
# 이미 articles와 user의 1:N 관계에 대한 정의는 create 뷰함수에서 완료
# 하지만 "권한"에 대한 설정은 필요함. 다른사람이 내 글 수정할 수 있으면 안되니까!

@login_required
def update(request, pk):    
    article = Article.objects.get(pk=pk)
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'article': article,
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    return redirect('articles:detail', article.pk)

@login_required
@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user == article.user:
            article.delete()
            return redirect('articles:index')
        return redirect('articles:detail',article.pk)