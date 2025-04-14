from . import views
from django.urls import path

app_name = 'restaurants'

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:res_pk>/',views.detail,name='detail'),
    path('create_restaurants/',views.create_restaurants,name='create_restaurants'),
]