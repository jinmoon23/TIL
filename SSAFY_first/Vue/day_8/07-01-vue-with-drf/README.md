# day_8 django with vue

django를 백엔드로 구성하고 vue로 데이터를 전달하여 사용자에게 보여주는 구성.

1. bash 터미널을 2개로 나눠 좌측은 django / 우측은 vue 구성
2. 각자의 서버를 오픈!
3. drf 서버로의 AJAX 요청을 위한 (vue)axios 설치 및 관련 코드 작성
4. axios 설치 후 요청하면 CORS Policy에 의해 막힘
5. 모든 브라우저는 기본적으로 동일 출처 정책(Same-Origin Policy)을 따르기 때문.


## Origin(출처)
Protocol / Host / Port를 모두 포함하여 출처라고 함.
CORS: 다른 출처의 자원에 접근할 수 있는 권한을 부여하도록 브라우저에게 알려주는 체계. 서버가 브라우저에게 알려준다.

예를들어 서버가 브라우저에게 `A도메인`은 우리 서버에 접근할 수 있습니다~ 라고 알려주는 것.

결론. 서버(Django)가 CORS 헤더를 설정해야 한다. -> `settings.py` 
