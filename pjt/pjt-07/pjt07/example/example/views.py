from django.shortcuts import render
import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .serializers import WeatherSerializer
from .models import Weather
# Create your views here.
# 1. openWeatherMap API 로부터 데이터 다운로드

# 2. 그대로 출력
@api_view(['GET'])
def index(request):
    # 3. API_KEY는 노출되면 안됨! 특히 깃허브에
    # 그럼 어떻게 숨길 수 있을까?
    # environ 설정을 통해 숨길 수 있다.
    API_KEY = settings.API_KEY
    city_name = 'seoul,kr'
    URL = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}'
    response = requests.get(URL).json()
    return Response(response)

def save_data(request):
    # 1. API를 통해 데이터를 가져옴
    API_KEY = settings.API_KEY
    city_name = 'seoul,kr'
    URL = f'https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_KEY}'
    response = requests.get(URL).json()
    # 2. 원하는 필드만 꺼내서
    for li in response.get('list'):
        dt_txt = li.get('dt_txt')
        temp = li.get('main').get('temp')
        feels_like = li.get('main').get('feels_like')
    # 3. db에 없다면(중복 데이터를 미연에 방지하는것이 좋음!)
        # 만약 중복된다면 continue
        if Weather.objects.filter(dt_txt=dt_txt,temp=temp,feels_like=feels_like).exists():
            continue
        # 중복되지 않는 데이터라면 저장
        else:
            data = {   
                'dt_txt': dt_txt,
                'temp': temp,
                'feels_like':feels_like,
            }
            serializer = WeatherSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                # 4. 저장한다.
                serializer.save()
    return JsonResponse({
        'message': '저장 성공!'
    })