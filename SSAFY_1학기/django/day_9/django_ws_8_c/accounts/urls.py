from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    # 1. 로그아웃 요청을 받을 url 설정
    path('logout/', views.logout, name='logout'),
]