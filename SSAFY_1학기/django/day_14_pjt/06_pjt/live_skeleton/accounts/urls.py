from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]


# 1. 회원가입
# 2. 로그인 / 로그아웃
# 3. 게시글: 작성자 및 staff만 삭제 및 수정 가능
# 4. 댓글: 작성자 및 staff만 삭제 및 수정 가능