# 관통 프로젝트(PJT)
- 소개: 지금까지의 강의 내용을 복습함과 동시에 더 나아가 활용해보는 시간
- 확정 전까지 두 가지 버전 중 어떤 프로젝트를 해도 상관없음! 최대한 두 버전 **다 해보는 쪽으로** 해보자.
- 프로젝트는 **개인 단위**로 진행함!

## PJT01
- 포인트: API 이해하기 / 날씨데이터 가져오기
- API 이해하기
  - 서버와 클라이언트
    - 서버: 부탁을 **받는** 역할
    - 클라이언트: 부탁을 **하는** 역할
  - .json(): 내부 데이터를 JSON 형태(dict와 비슷, **왜 비슷인거지?**)로 변환해주는 함수
  - 다양한 방식으로(크롬 또는 파이썬 등) 서버에 요청을 보낼 때 서버는 어떻게 구별해서 데이터를 보낼 것인가? -> **API의 존재이유**
  - **서버 입장에서 API를 미리 만들어 둔 후** 클라이언트단에서 요청을 보내면 API를 거쳐 서버단으로 요청이 전달되고 데이터 또한 API를 거쳐 클라이언트단으로 전달된다.
- 날씨데이터 가져오기
  - 필요한 정보: 날씨데이터를 보유한 서버 / 해당 서버의 API
  - 사용할 서버
    - openweathermapapi / 금융정보
- GPT를 활용하여 프로젝트를 진행할 때는 항상 **공식문서와 함께** 보면서 해야함!

### JSON
- 데이터를 저장하거나 전송할 때 많이 사용되는 **경량의 텍스트 기반 데이터 형식**
- 키는 문자열 / 값은 다양한 데이터 유형 / 쉼표로 구분
- 파이썬의 dic를 닮은 **문자열**

## 제출 시 주의사항
- 금일 18시까지 제출
- 반드시 README.md에 단계별 구현 중 힘들었던 점, 새로 배운 점들을 상세히 기록하여 제출
- 깃랩에 제출 / 이름은 01-pjt 형식
- 뉴 프로젝트 누른 후 blank 프로젝트로 생성 후 제출