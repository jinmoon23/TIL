from django.urls import path
from . import views

app_name = 'example'

urlpatterns = [
    path('',views.index,name='index'),
    path('save_data/',views.save_data,name='save_data'),
]