from rest_framework import serializers
from .models import Location, Station, Car


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = '__all__'
        # read_only_fields = ('address', )
    class locationAddressSerializer(serializers.ModelSerializer):
        class Meta():
            model = Location
            fields = ['address',]
    # 변수명 설정이 중요하다! 모델에 설정한 
    # 변수명과 동일해야 함!        
    address = locationAddressSerializer(read_only=True)

class StationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        fields = ('address', 'is_opening',)
        

        