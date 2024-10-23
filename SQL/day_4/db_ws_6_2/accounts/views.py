from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import CustomUserCreationForm
# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            # 회원가입과 다른 점을 기억하자
            user = form.get_user
            auth_login(request,user)
            return redirect('libraries:root')
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
            return redirect('libraries:root')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/signup.html',context)