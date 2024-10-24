from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            # 회원가입과 다른 점을 기억하자
            user = form.get_user()
            auth_login(request,user)
            return redirect('root')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/login.html',context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 로그인과 다른 점을 기억하자
            user = form.save()
            auth_login(request,user)
            return redirect('root')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/signup.html',context)

def logout(request):
    if request.method == 'POST':
        auth_logout(request)
    return redirect('root')

def signout(request):
    if request.method == 'POST':
        request.user.delete()
    return redirect('root')