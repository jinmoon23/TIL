from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()
# Create your views here.
def index(request):
    members = User.objects.all()
    context = {
        'members': members
    }
    return render(request, 'accounts/index.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('stores:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('accounts:login')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('stores:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
def update(request):
    if request.method == 'POST':
        # 1. 유저가 수정한 정보를 받아옴
        change_form = CustomUserChangeForm(request.POST,instance=request.user)
        # 2. 얘 잘 수정했나?
        if change_form.is_valid():
            # 3. 회원가입과 달리 로그인 해주는 과정 안해도 됨!
            # 이미 로그인 상태니까!
            change_form.save()
            return redirect('accounts:index')
    else:
        # 유저 정보 수정의 특이한 점
        # article의 경우 instance=article 처럼 인스턴스가 들어갔었음 
        change_form = CustomUserChangeForm(instance=request.user)
    context = {
        'change_form': change_form,
    }
    return render(request,'accounts/update.html',context)