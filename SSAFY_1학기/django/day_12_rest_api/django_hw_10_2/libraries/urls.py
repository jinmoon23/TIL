from django.urls import path
from . import views

urlpatterns = [
    path('libraries/',views.index),
    path('libraries/<int:book_pk>/',views.detail),
]
