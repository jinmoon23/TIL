from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
# 2. django에서 제공하는 로그아웃 메서드 import
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
# from .forms import LoginForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    # 4. import 했던 로그아웃 메서드 사용
    # 해당 메서드를 타고 들어가보면 알 수 있듯이 인자를 request 하나만 받는다.
    # 왜냐하면 로그인 되어 세션에 등록된 유저는 하나 뿐이기 때문.
    auth_logout(request)
    return redirect('accounts:login')