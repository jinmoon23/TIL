from django.shortcuts import render, redirect
from .models import Diary, Comment
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comment_form = CommentForm()
    context = {
        'diaries': diaries,
        'comment_form': comment_form
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def comments_create(request, diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.diary = diary
            comment.save()
    return redirect('diaries:index')

def comments_delete(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('diaries:index')

def likes(request,diary_pk):
    diary = Diary.objects.get(pk=diary_pk)
    user = request.user
    if request.method == 'POST':
        # 좋아요 누르는 유저(request.user)가
        # 해당 diary에 대해 좋아요를 누른 목록에 있는 유저라면
        # 해당 동작은 좋아요를 취소하는 것. 
        if user in diary.like_users.all():
            diary.like_users.remove(user)
        else:
            diary.like_users.add(user)
    return redirect('diaries:index')