from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.
def login(request):
    # 로그인 하는 로직을 시작해 달라!
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        # 만약 인증된 사용자라면 로그인 진행(세션 데이터 생성)
        if form.is_valid():
            # 인증된 유저 객체는 어디에 있나? 바로 form에 있다~!!
            # 그런데 어떻게 그 객체만 뽑아오지? 바로 get_user() 메서드로~!!
            user = form.get_user()
            auth_login(request, user=user)
            return redirect('articles:index')
    # 로그인 페이지 자체를 달라!
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    # 세션 데이터 삭제
    auth_logout(request)
    return redirect('articles:index')