from django.shortcuts import render,redirect
# 2. 이제 아래의 form을 사용하지 않고 AuthenticationForm를 새롭게 import 하여 사용할 것임.
# from .forms import LoginForm
from django.contrib.auth.forms import AuthenticationForm
# 6. 로그인을 진행하는 django의 빌트인 메서드를 import 하여 로그인 진행
from django.contrib.auth import login as auth_login

# Create your views here.
def login(request):
    # 로그인 로직을 실행해 주세요~!
    if request.method == 'POST':
        # 3. 첫 번째 인자로 request를 받고 두 번째 인자로 입력 data를 받는다.
        form = AuthenticationForm(request,data=request.POST)
        # 4. 유효성 검사를 실시하고
        if form.is_valid():
            # 5. 적절한 로그인 요청이라면 로그인을 진행한다.
            # 6. form에 저장된 user를 객체로 저장한다.
            user = form.get_user()
            # import한 로그인 메서드를 사용한다. 
            auth_login(request,user=user)
            return redirect('todos:index')
    # 로그인 페이지 자체를 주세요~!
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request,'accounts/login.html',context)