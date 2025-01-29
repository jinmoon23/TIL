from django.shortcuts import render,redirect
from .models import Memo
from .forms import MemoForm
# Create your views here.

def index(request):
    memos = Memo.objects.all()
    context = {
        'memos': memos
    }
    return render(request,'index.html',context)

def detail(request,pk):
    memo = Memo.objects.get(pk=pk)
    context = {
        'memo': memo,
    }
    return render(request,'detail.html',context)

def create(request):
    if request.method == 'POST':
        # 1. form으로 받아온 입력값을 변수에 담음
        # request.POST == querydict -> 입력값이 딕셔너리 형태로 넘어옴
        form = MemoForm(request.POST)
        # 2. 유효성 검사
        if form.is_valid():
            # 3. 저장
            memo = form.save()
            context = {
                'memo': memo
            }
            return render(request,'detail.html',context)
    else:
        form = MemoForm()
    context = {
        'form' : form,
    }
    return render(request,'create.html',context)

def delete(request,pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return redirect('memos:index')