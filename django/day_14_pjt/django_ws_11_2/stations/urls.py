from django.urls import path
from . import views
urlpatterns = [
    path('stations/',views.station_list),
    path('locations/<int:location_pk>/stations/',views.station),
    path('stations/<int:station_pk>/',views.station_detail),
    path('locations/',views.location_list),
]
