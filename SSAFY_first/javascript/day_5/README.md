# Day_5

## 배열
Object는 key로 구분된 데이터 집합을 저장. 이제는 순서가 있는 데이터 구조가 필요.
특징
  - 요소값에 대한 자료형 제약 없음
주요 메서드
- pop / push: 배열의 맨 끝 조작
- shift / unshift: 배열의 맨 앞 조작

## Array Helper Method
특징
  - 배열의 각 요소를 `순회`하며 각 요소에 대해 함수(콜백함수)를 호출
    - 콜백함수? 다른 `함수`에 `인자로 전달`되는 `함수`
    - 단순화된 형태 : `func(콜백함수)`
  - 대표 메서드
    - `foreach()`, `map()`, filter(), every(), some(), reduce()...
  - 메서드 호출 시 인자로 `함수`를 받는다.

## foreach()와 map()
- 매우 비슷하지만 `foreach()`는 반환이 없다.
- `map()`은 순회 하면서 콜백함수를 적용한 후 모아모아 새로운 배열을 반환한다. -> return이 필요함!

## 다양한 순회문의 차이 종합
- for loop
  - 인덱스로 배열 접근
  - break / continue 사용 `가능`
- for ... of
  - 배열의 요소에 곧바로 접근
  - break / continue 사용 `가능`
- foreach()
  - 간결하고 가독성이 높음
  - break / continue 사용 `불가능` -> some과 every를 활용해 비슷한 동작을 구현할 수 있다. 
