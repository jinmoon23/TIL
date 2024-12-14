from django.shortcuts import render, redirect
from .models import Diary, Comment
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comments = Comment.objects.all()
    form = CommentForm()
    context = {
        'diaries': diaries,
        'form': form,
        'comments': comments,
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

def create_comment(request,diary_pk):
    # 1. 어떤 일기에 댓글을 달거야? -> pk를 활용해 일기 조회
    diary = Diary.objects.get(pk=diary_pk) 
    # 2. comment_form에 어떤 내용이 담겨있어?
    comment_form = CommentForm(request.POST)
    # 3. 유효성검사 실시 -> 이상없으면 해당 내용으로 저장 후 redirect
    if comment_form.is_valid():
        # 4. 여기서 추가적인 코드를 작성하지 않으면 integrity error가 발생함
        # 원인은? foreignKey를 설정했는데 그 값을 설정하지 않았기 때문
        # 쉽게말해 django는 어떤 diary에 대한 comment인지를 아직 모르고 있다!
        # comment_form.save()
        
        # 6. 어떤 diary인지를 알 수 있도록 인스턴스를 반환하여 변수에 담되
        # 곧바로 save() 메서드를 수행하지는 않는다. -> commit=False
        comment = comment_form.save(commit=False)
        
        # 7. foreignKey 정보를 담고있는 인스턴스를 통째로 저장해준다.
        comment.diary = diary
        
        # 8. 비로소 save() 하면 저장 완료~
        comment.save()
        return redirect('diaries:index')
    # 5. 유효성 검사 통과못하면 다시 index 페이지 보여줘
    return redirect('diaries:index')