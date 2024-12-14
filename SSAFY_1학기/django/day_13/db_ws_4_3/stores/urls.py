from django.urls import path
from . import views


app_name = 'stores'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:store_pk>/', views.detail, name='detail'),
    path('create_store/', views.creates_store, name='creates_store'),
    path('<int:store_pk>/create_product/', views.creates_product, name='creates_product'),
]
