from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationsForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
@require_http_methods(['GET','POST'])
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationsForm(request.POST)
        if form.is_valid():
            # 1. user는 CustomUserCreationsForm에 들어있다!
            user = form.save()
            # 2. 로그인 진행
            # 1의 user를 2번째 인자로 넣어준다!
            auth_login(request,user)
            return redirect('boards:index')
    else:
        form = CustomUserCreationsForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/signup.html',context)

@require_http_methods(['GET','POST'])
def login(request):
    if request.method == 'POST':
        # 1. 첫 인자로 request!!
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            # 2. singup과 다른점 주의!! form.save()와 form.get_user()
            user = form.get_user()
            auth_login(request,user)
            next = request.GET.get('next')
            if next:
                return redirect(next)
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/login.html',context)

@require_http_methods(['POST'])
def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('boards:index')