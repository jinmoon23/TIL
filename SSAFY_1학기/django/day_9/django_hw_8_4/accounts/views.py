from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User
# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request,'accounts/index.html',context)

def login(request):
    # 로그인 로직을 실행해 주세요~
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user=user)
            return redirect('accounts:index')
    # 로그인 페이지 자체를 주세요~
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')