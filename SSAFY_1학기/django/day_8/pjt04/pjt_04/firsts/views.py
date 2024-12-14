from django.shortcuts import render
import matplotlib.pyplot as plt
# io : 입출력 연산을 위한 파이썬 표준 라이브러리
from io import BytesIO
# 텍스트 <-> 이진 데이터 변환해주는 모듈
import base64
import pandas as pd
from .models import Weather

# Create your views here.
def index(request):
    x = [1,2,3,4,5]
    y = [2,4,6,8,10]
    # 그래프 초기화
    plt.clf()
    # 그래프 그리기
    plt.plot(x,y) 
    plt.title('Test Graph')
    plt.ylabel('y label')
    plt.xlabel('x label')
    # 예전 출력 방식
    # plt.show() 
    # 1. 비어있는 버퍼 생성
    buffer = BytesIO()
    # 2. 버퍼에 그래프를 저장
    plt.savefig(buffer,format='png')
    # 3. 버퍼의 내용을 base64를 활용하여 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n','')
    buffer.close()
    context = {
        'chart_image':f'data:image/png;base64,{image_base64}',
    }
    return render(request,'firsts/index.html',context)


def example(request):
    # 1. csv 파일 읽기(pandas)
    csv_path = 'firsts/data/test_data.csv'
    df = pd.read_csv(csv_path)
    print(df)
    # 2. DB에 저장(복습용임 ㅎㅎ)
    for index,row in df.iterrows():
        if Weather.objects.filter(date=row['Date']).exists():
            continue
        weather = Weather(
            date=row['Date'],
            temp_avg_f=row['TempAvgF'],
            # Events 필드는 결측치를 포함
            events=row['Events'] if pd.notna(row['Events']) else ""
        )
        # - 중복된 데이터는 저장하지 않도록 구성하는 것이 중요
        weather.save()
    
    weathers = Weather.objects.all()
    context = {
        'weathers':weathers
    }
    return render(request,'firsts/example.html',context)