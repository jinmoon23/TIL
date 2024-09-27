from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dt
from .models import Weather
import base64
from io import BytesIO
import numpy as np
# Create your views here.

csv_path = 'weathers/data/austin_weather.csv'
df = pd.read_csv(csv_path)

for index,row in df.iterrows():
    if Weather.objects.filter(date=row['Date']).exists(): continue
    weather = Weather(
        date = row['Date'],
        temp_high_f = row['TempHighF'],
        temp_avg_f = row['TempAvgF'],
        temp_low_f = row['TempLowF'],
        dew_point_high_f = row['DewPointHighF'] if row['DewPointHighF'] != '-' else 0,
        dew_point_avg_f = row['DewPointAvgF'] if row['DewPointAvgF'] != '-' else 0,
        dew_point_low_f = row['DewPointLowF'] if row['DewPointLowF'] != '-' else 0,
        humidity_high_percent = row['HumidityHighPercent'] if row['HumidityHighPercent'] != '-' else 0,
        humidity_avg_percent = row['HumidityAvgPercent'] if row['HumidityAvgPercent'] != '-' else 0,
        humidity_low_percent = row['HumidityLowPercent'] if row['HumidityLowPercent'] != '-' else 0,
        sea_level_p_high_inches = row['SeaLevelPressureHighInches'] if row['SeaLevelPressureHighInches'] != '-' else 0,
        sea_level_p_avg_inches = row['SeaLevelPressureAvgInches'] if row['SeaLevelPressureAvgInches'] != '-' else 0,
        sea_level_p_low_inches = row['SeaLevelPressureLowInches'] if row['SeaLevelPressureLowInches'] != '-' else 0,
        events = row['Events'],
    )
    weather.save()

def problem_1(request):
    weathers = Weather.objects.all()
    context = {
        'weathers':weathers,
    }
    return render(request,'weathers/problem1.html',context)

def problem_2(request):
    # 1. 잦은 새로고침의 경우를 대비해 그래프 초기화
    plt.clf()
    # 2. 2차원 그래프의 x축과 y축을 설정
    plt.plot(df['Date'], df['TempHighF'], label = 'High Temperature')
    plt.plot(df['Date'], df['TempAvgF'], label = 'Avg Temperature')
    plt.plot(df['Date'], df['TempLowF'], label = 'Low Temperature')
    # 3. 그래프의 디자인적 요소 설정
    # label에 따라 범례를 설정
    plt.legend()
    # x축의 가독성을 위해 label을 회전
    plt.xticks(rotation=45)
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    # 4. datetime으로 구성된 x축 value의 간격을 보기 좋게 설정
    ax = plt.gca()
    ax.xaxis.set_major_locator(dt.MonthLocator(interval=3))
    # plt.show()
    # 5. 비어 있는 버퍼 생성
    buffer = BytesIO()
    # 6. 버퍼에 그래프를 저장
    plt.savefig(buffer,format='png')
    # 7. 버퍼의 내용을 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    context = {
        'chart_image': f'data:image/png;base64,{image_base64}',
    }
    return render(request,'weathers/problem2.html',context)

def problem_3(request):
    df['Date'] = pd.to_datetime(df['Date'])
    monthly_data = df.groupby(df['Date'].dt.to_period('M')).mean()
    
    plt.plot(monthly_data['Date'], monthly_data['TempHighF'], label = 'Monthly High Temperature AVG')
    plt.plot(monthly_data['Date'], monthly_data['TempAvgF'], label = 'Monthly Avg Temperature AVG')
    plt.plot(monthly_data['Date'], monthly_data['TempLowF'], label = 'Monthly Low Temperature AVG')
    plt.legend()
    plt.xticks(rotation=45)
    plt.title('Temperature Variation')
    plt.xlabel('Date')
    plt.ylabel('Temperature(Fahrenheit)')
    plt.show()