from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import matplotlib.pyplot as plt
import matplotlib
import base64
from io import BytesIO

matplotlib.use('Agg')
def get_google_data(keyword):
    url = f"https://www.google.com/search?q={keyword}"
    # Chrome 옵션 설정
    options = Options()
    options.add_argument('--headless')  # 브라우저를 숨기고 백그라운드에서 실행

    # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # 열린 페이지 소스를 받아옴
    html = driver.page_source 
    soup = BeautifulSoup(html, "html.parser")

    # div 태그 중 id 가 result-stats 인 요소 검색
    result_stats = soup.select_one("div#result-stats")

    driver.quit()
    return result_stats.text

# 키워드 저장 및 keyword.html로 렌더링
def keyword(request):
    keywords = Keyword.objects.all()
    if request.method == 'POST':
        form = KeywordForm(request.POST)
        if form.is_valid():
            # 동일한 키워드로 중복 저장되지 않도록 하는 로직
            name = form.cleaned_data.get('name')
            if not Keyword.objects.filter(name=name).exists():
                form.save()
                return redirect('trends:keyword')
            else:
                form.add_error('name','이미 존재하는 키워드입니다.')
    else:
        form = KeywordForm()
    context = {
        'form' : form,
        'keywords': keywords,
    }
    return render(request, 'trends/keyword.html', context)

# 키워드 삭제 및 keyword.html로 리다이렉션
def keyword_detail(request,pk):
    keyword = Keyword.objects.get(pk=pk)
    keyword.delete()
    return redirect('trends:keyword')

# 크롤링 수행 및 crawling.html 렌더링
def crawling(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        # '검색결과 약 xx개' 형태의 문자열
        dummy = get_google_data(keyword.name)
        int_lst = []
        for char in dummy:
            if char == '(':
                break
            if char.isdigit():
                int_lst.append(char)
        # 검색결과의 개수 정수값
        result = int(''.join(int_lst))
        name = keyword.name
        search_period = 'all'
        trend, created_trend = Trend.objects.get_or_create(name=name, defaults={
            'result': result,
            'search_period': search_period
            }
        )
    trends = Trend.objects.all()
    context = {
        'trends':trends,
    }
    return render(request,'trends/crawling.html',context)

# 크롤링 수행 후 수행결과 막대 그래프 생성 및 crawling_histogram.html 렌더링
def crawling_histogram(request):
    # 1. 트렌드 데이터 가져오기
    trends = Trend.objects.all()

    # 2. name과 result 값 분리
    names = [trend.name for trend in trends]
    results = [trend.result for trend in trends]

    # 3. 막대 그래프 그리기
    plt.figure(figsize=(10,6))  # 그래프 크기 설정
    plt.bar(names, results, label='Trends')

    # 4. 그래프 레이블 설정
    plt.xlabel('Keyword')
    plt.ylabel('Result')
    plt.title('Technology Trend Analysis')
    plt.xticks(rotation=45)  # 이름이 겹치지 않도록 45도 회전
    plt.legend(loc='upper right') # 범례 위치 설정

    # plt.show
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

    return render(request,'trends/crawling_histogram.html', context)


# 지난 1년을 기준으로 크롤링 수행 후 수행 결과 막대 그래프 생성 및 crawling_advanced.html 렌더링
def crawling_advanced(request):
    pass