﻿from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('search/',views.search),
    path('throw/',views.throw),
    path('catch/',views.catch),
    path('hello/<str:name>/',views.greeting)
]