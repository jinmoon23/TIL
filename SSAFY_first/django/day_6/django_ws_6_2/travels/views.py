from django.shortcuts import render,redirect
from .models import Travels
from .forms import TravelForm

# Create your views here.
def index(request):
    travels = Travels.objects.all()
    context = {
        'travels':travels,
    }
    return render(request,'index.html',context)

def create(request):
    # 유저가 제출 버튼을 누른 경우 -> DB에 저장 및 확인하는 페이지 필요
    if request.method == 'POST':
        # 첫번째 인자가 data이기 때문에 키워드 작성하지 않음
        form = TravelForm(request.POST)
        if form.is_valid():
            travel = form.save()
            return redirect('travels:detail',travel.pk)
            # return render(request,'travels/index')
    # 유저가 create 버튼을 누른 경우 -> 생성하는 html 렌더링 필요 
    else:
        form = TravelForm()
    context = {
        'form': form,
    }
    return render(request, 'create.html',context)

def detail(request,pk):
    travel = Travels.objects.get(pk=pk)
    context = {
        'travel':travel,
    }
    return render(request,'detail.html',context)