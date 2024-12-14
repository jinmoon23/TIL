from django.shortcuts import render,redirect
# 로그인을 위한 form
from django.contrib.auth.forms import AuthenticationForm
# 유효성 검사 후 로그인 세션을 생성하는 함수 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# 유저 회원가입을 위한 form -> 이거 사용하면 안됨!
# from django.contrib.auth.forms import 
# 내가 custom한 회원가입 폼을 import 해오자!
from .forms import CustomUserCreationForm
from .models import User
# Create your views here.
def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request,request.POST)
        if login_form.is_valid():
            auth_login(request,login_form.get_user())
            return redirect('stores:index')
    else:
        login_form = AuthenticationForm()
    context = {
        'login_form': login_form,
    }   
    return render(request,'accounts/login.html',context)

def sign_up(request):
    if request.method == 'POST':
        sign_up_form = CustomUserCreationForm(request.POST)
        if sign_up_form.is_valid():
            user = sign_up_form.save()
            auth_login(request,user)
            return redirect('stores:index')
    else:
        sign_up_form = CustomUserCreationForm()
    context = {
        'sign_up_form': sign_up_form,
    }
    return render(request,'accounts/sign_up.html',context)

def logout(request):
    auth_logout(request)
    return redirect('stores:index')

def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request,'accounts/index.html', context)