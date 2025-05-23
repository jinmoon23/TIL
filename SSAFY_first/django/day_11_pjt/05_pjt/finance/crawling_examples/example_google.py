from bs4 import BeautifulSoup
import requests

def crawling_basic(keyword):
    # 가져올 url 문자열로 입력
    url = f'https://www.google.com/search?q={keyword}'  

    # 크롬 브라우저가 열린다. 이 때, 동적인 내용들이 모두 채워짐
    driver = webdriver.Chrome()
    driver.get(url)
    # requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
    response = requests.get(url)   
    # print(response)
#     # 우리가 얻고자 하는 html 문서가 여기에 담기게 됨
    html_text = response.text
    print(html_text)
    with open('soup.txt','w',encoding='utf-8') as file:
        file.write(html_text)

#     # html을 잘 정리된 형태로 변환
    soup = BeautifulSoup(html_text, 'html.parser')
    # 보기 좋은 형태로 프린트
    # print(soup.prettify)
    
#     # 1. 태그를 이용하여 하나 검색
    # main = soup.find('a')
    # print(f'제목 : {main.text}')

#     # 2. 해당 태그인 모든 요소 검색
    a_tags = soup.find_all('a')
    # 리스트 형태로 반환 -> iterable 
    # print(f'a 태그 : {a_tags}')
    # 반복문을 활용한 경우
    # for tag in a_tags:
    #     print(f'태그: {tag.text}')

#     # 3. CSS 선택자로 하나 검색
#     # 선택자가 일치하는 첫 번째글
    word = soup.select_one('.text')
    # print(f'첫 번째 글 = {word.text}')

#     # 4. CSS 선택자로 여러 개 검색하기
    words = soup.select('.text')
    # for w in words:
        # print(f'글 : {w.text}')

#     # 예쁘게 출력하기
#     # print(soup.prettify())

keyword = '탕수육'
crawling_basic(keyword)