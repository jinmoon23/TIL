from django.shortcuts import render, redirect
from .models import Keyword, Trend
from .forms import KeywordForm
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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
        form.save()
        # keyword, created = Keyword.objects.get_or_create(form)
        return redirect('trends:keyword')
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

# 크롤링 수행 및 crawling.html로 리다이렉션
def crawling(request):
    keywords = Keyword.objects.all()
    for keyword in keywords:
        # '검색결과 약 xx개' 형태의 문자열
        dummy = get_google_data(keyword)
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
        # 이렇게 해도 중복제거가 안된다.. 이유가 뭘까..ㅜㅜ
        trend, created_trend = Trend.objects.get_or_create(name=name,result=result,search_period=search_period)
        # trend = Trend(name=name,result=result,search_period=search_period)
    trends = Trend.objects.all()
    context = {
        'trends':trends,
    }
    return render(request,'trends/crawling.html',context)

# 크롤링 수행 후 수행결과 막대 그래프 생성 및 crawling_histogram.html 렌더링
def crawling_histogram(request):
    pass

# 지난 1년을 기준으로 크롤링 수행 후 수행 결과 막대 그래프 생성 및 crawling_advanced.html 렌더링
def crawling_advanced(request):
    pass