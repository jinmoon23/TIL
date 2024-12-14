from django.shortcuts import redirect, render, get_object_or_404
from .models import Travel
from .forms import TravelForm
from django.views.decorators.http import require_http_methods, require_safe

# Create your views here.

@require_safe
def index(request):
    travels = Travel.objects.all()
    context = {
        'travels':travels
    }
    return render(request,'travels/index.html',context)

@require_http_methods(["GET","POST"])
def create(request):
    if request.method == 'POST':
        form = TravelForm(request.POST)
        if form.is_valid:
            travel = form.save()
            return redirect('travels:detail',travel.pk)
    else:
        form = TravelForm()
    context={
        'form':form
    }
    return render(request,'travels/create.html',context)

@require_safe
def detail(request,pk):
    travel = get_object_or_404(Travel,pk=pk)
    context = {
        'travel':travel
    }
    return render(request,'travels/detail.html',context)

def delete(request,pk):
    travel = Travel.objects.get(pk=pk)
    travel.delete()
    return redirect('travels:index')

def update(request,pk):
    travel = Travel.objects.get(pk=pk)
    # 유저가 수정페이지에서 수정 버튼을 최종적으로 누른 경우
    if request.method == 'POST':
        # 기존에 작성된 데이터를 인스턴스로 넣어줘야만 장고 폼이 
        # 아 이게 수정이구나! 를 알게됨
        form = TravelForm(request.POST,instance=travel)
        if form.is_valid():
            form.save()
            return redirect('travels:detail', travel.pk)
    else:
        # 유저가 디테일페이지에서 수정버튼을 눌러 수정페이지 접근 시
        # 기존에 작성된 상태를 받아옴 
        form = TravelForm(instance=travel)
    context = {
        'form': form,
        'travel': travel,
    }
    return render(request,'travels/update.html',context)

