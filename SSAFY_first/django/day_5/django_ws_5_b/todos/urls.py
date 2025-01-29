from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_todo/', views.create_todo, name='create_todo'),
    path('<int:todo_pk>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    # 생성의 경우를 제외한 모든 경우 아래와 같이 경로에 유의해야 함.  
    path('<int:todo_pk>/delete/',views.delete, name = 'delete'),
]