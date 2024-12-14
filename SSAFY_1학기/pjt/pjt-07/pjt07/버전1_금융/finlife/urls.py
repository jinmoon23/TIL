from django.urls import path
from . import views

app_name = 'finlife'

urlpatterns = [
    path('api_test/',views.index,name='index'),
    path('save/',views.save_data,name='save_data'),
    path('deposit_products/',views.deposit_products,name='deposit_products'),
]
