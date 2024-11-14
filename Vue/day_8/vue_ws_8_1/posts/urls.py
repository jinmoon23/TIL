from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.postList_or_create),
    path('categories/', views.categoryList_or_create),
    path('<int:post_pk>/comment/',views.comment),
]
