from rest_framework import serializers
from .models import Station, Location

class StationListSerializers(serializers.ModelSerializer):
    class Meta():
        model = Station
        fields = ['address','is_opening']
        read_only_fields = ['address',]
class StationSerializers(serializers.ModelSerializer):
    class Meta():
        model = Station
        fields = '__all__'
        read_only_fields = ['address',]
class LocationListSerializers(serializers.ModelSerializer):
    class Meta():
        model = Location
        fields = '__all__'