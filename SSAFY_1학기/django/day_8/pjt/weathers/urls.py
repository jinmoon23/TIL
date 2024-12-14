from django.urls import path
from . import views

app_name = 'weathers'

urlpatterns = [
    path('problem1/', views.problem_1, name='problem1'),
    path('problem2/', views.problem_2, name='problem2'),
    path('problem3/', views.problem_3, name='problem3'),
]