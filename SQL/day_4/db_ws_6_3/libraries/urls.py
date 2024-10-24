from django.urls import path
from . import views


app_name = 'libraries'

urlpatterns = [
    path('novels/', views.novels, name='novels'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_novel/', views.create_novel, name='create_novel'),
]