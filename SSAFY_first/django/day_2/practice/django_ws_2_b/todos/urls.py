from django.urls import path
from . import views

app_name = 'todos'
    
urlpatterns = [
    path("index/", views.index, name = 'index'),
    path("create_todo/", views.create_todo, name = 'create_todo'),
]