# API
두 소프트웨어가 서로 통신할 수 있게 하는 메커니즘
"이렇게 요청을 보내면, 이렇게 응답을 줄 것이다" 라는 메뉴얼
## 역할
복잡한 코드를 추상화하여 보다 간단히 사용할 수 있는 구문을 제공
## 활용
요즘은 다~ open API를 활용해서 개발을 한다 이말이다~!
## API Server 설계의 방법론 == REST
REST: Representational State Transfer
**자원을 정의**하고 자원에 대한 **주소를 지정**하는 전반적인 `방법` 서술

자원을 정의?
- 자원의 `식별`: URI
- 자원의 `행위`: HTTP METHOD
- 자원의 `표현`: JSON DATA

자원의 식별?
- URI: 통합 자원 **식별자** -> 통상적으로 url
- 네트워크 상 리소스(자원)의 주소(위치)
- 맨 앞: Schema or Protocol -> 규약
- 두 번째: Domain Name -> 원래 IP주소로 접근해야 하지만 이러면 외워서 사용하기 힘들기 때문에 이런 방식으로 사용
- 세 번째: Port -> 웹 서버의 자원에 접근하기 위한 기술적인 문
- 네 번째: Path -> 자원에 대한 접근 경로 
- ? 이후: Parameters -> 웹 서버에 제공하는 추가적인 데이터

자원의 행위?
- HTTP Request Methods : 자원에 대한 행위를 정의
- GET / POST / PUT / DELETE
- Read / Create / Update / Delete

자원의 표현?