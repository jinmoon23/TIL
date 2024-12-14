from django.shortcuts import render, redirect
# 로그인과 인증 / 권한에 대한 import
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserCreationsForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    # 이미 로그인 한 사용자라면 접근할 수 없도록 한다. 
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    # 이미 로그인 한 사용자라면 접근을 제한
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationsForm()   
    context = {
        'form': form
    }
    return render(request,'accounts/signup.html',context)
@login_required
def delete(request):
    # User 모델에서 누가 회원탈퇴를 요청한건지 검색해야 할 것 같지만
    # 그러지 않아도 된다. 그 이유는 request에 User 객체가 들어있기 때문.
    user = request.user
    user.delete()
    # request.user.delete() -> 이와같은 형식도 가능
    return redirect('articles:index')
@login_required
def update(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=user)
    context = {
        'form':form,
    }
    return render(request,'accounts/update.html',context)

# 인자의 구성이 다름에 주의
@login_required
def password(request,user_pk):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(user,request.POST)
        if form.is_valid():
            form.save()
            # 옵션임!
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(user)  
    context = {
        'form':form,    
    }
    return render(request,'accounts/password.html',context)