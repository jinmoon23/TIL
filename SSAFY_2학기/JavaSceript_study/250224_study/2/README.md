# 변수
- 컴퓨터는 메모리 셀의 크기, 즉 1바이트 단위로 데이터를 저장하거나 읽어들인다. 
- 메모리 주소를 통해 값에 직접 접근하려는 시도는 올바른 방법이 아니다. 이를 위해 프로그래밍 언어는 기억하고 싶은 값을 메모리에 저장하고, 저장된 값을 읽어 들여 재사용하기 위해 변수라는 메커니즘을 제공한다.
- 간단히 말해 값의 위치를 가리키는 상징적인 이름. 

## 호이스팅
```js
console.log(score); // undefined

var score;
```
- 변수 `선언`은 소스코드가 한 줄씩 순차적으로 실행되는 시점인 런타임에 실행되는 것이 아니라 `그 이전 단계에서 먼저` 실행된다. 

## 문과 표현식
문(Statement)
- 프로그램을 구성하는 기본 단위이자 최소 실행 단위.
- 문은 여러 토큰으로 구성됨. 토큰이란 문법적인 의미를 가지며, 문법적으로 더 이상 나눌 수 없는 코드의 기본 요소를 의미함.
- 문을 `명령문`이라고도 부른다.

## 데이터 타입
- 데이터 타입이 필요한 이유
  - 값을 `저장할 때 확보`해야 하는 메모리 공간의 크기를 결정하기 위해
  - 값을 `참조할 때 한 번에 읽어 들여야 할` 메모리 공간의 크기를 결정하기 위해
  - 메모리에서 읽어 들인 `2진수를 어떻게 해석`할지 결정하기 위해 
- 기본적으로 변수는 타입을 가지지 않는다. 하지만 값은 타입을 갖는다. 따라서 현재 변수에 할당되어 있는 값에 의해 변수의 타입이 동적으로 결정된다. 
- 즉 이러한 동적타입언어인 자바스크립트는 유연성은 높지만 신뢰성은 떨어진다. 

## null에 대한 typeof 연산
- null이 아닌 object를 반환함. 이는 초기 자바스크립트의 버그임. 기존 코드에 영향을 줄 수 있기 때문에 아직 수정되지 않고 있다. 