# PJT-05 

## 웹 크롤링
1. 웹 페이지 다운로드
2. 페이지 파싱
   - 다운받은 코드를 **분석**하고 데이터 **추출**하는 단계
3. 링크 추출 및 다른 페이지 탐색
4. 데이터 추출 및 저장

준비단계
- 필수 라이브러리 설치
  - request
    - HTTP 요청을 보내고 응답을 받는 모듈
    - request.get(URL) -> HTTP의 GET요청을 한 것
  - beautifulsoup4
    - [Docs](https://beautiful-soup-4.readthedocs.io/en/latest/#quick-start)
    - find(): 태그를 사용하여 요소를 검색, 첫 번째로 일치하는 요소를 반환
    - find_all(): 태그를 사용하여 모든 요소를 검색
    - select(): CSS 선택자를 사용하여 요소를 검색. 모든 일치 요소를 반환
  - selenium
    - request 모듈은 정적인 부분만 다운가능 -> 서버가 이미 가지고 있는 데이터만 가능!
    - 따라서 동적인 부분 즉, 사용자가 검색하여 변동하는 부분을 다운로드 받을 수는 없다.
    - 이를 해결해주는 라이브러리가 selenium
    - 개발자들이 동적 웹 테스트를 위해서 사용한다. 