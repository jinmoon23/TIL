### 상속 클래스의 인스턴스 생성 과정
- 서브클래스는 자신이 직접 인스턴스를 생성하지 않고 수퍼클래스에게 인스턴스 생성을 위임한다. 이것이 바로 서브클래스의 constructor에게 반드시 super를 호출해야 하는 이유다.
- 하지만 new 연산자와 함께 호출된 클래스는 서브클래스다. 즉 new 연산자와 함께 호출된 함수를 가리키는 new.target은 서브클래스를 가리킨다. 따라서 인스턴스는 new.target이 가리키는 서브클래스가 생성한 것으로 처리된다. 
- 정리하면 인스턴스의 생성 자체는 수퍼클래스의 constructor가 처리하지만 new 연산자와 함께 인스턴스를 생성할 때는 서브클래스를 명시한다. 


# ES6 함수의 추가 기능
- ES6 이전의 함수는 모두 callable 이면서 constructor 였다. 이는 성능적인 면에서 많은 손해를 가져왔다.
- 이러한 문제를 해결하기 위해 ES6에서는 함수를 사용 목적에 따라 세 종류로 명확히 구분했다.
  - 일반 함수: 함수 선언문이나 함수 표현식으로 정의한 함수. 
  - 메서드: 객체에 바인딩된 함수
  - 화살표 함수: 간결한 구문과 상위 스코프의 this 값을 그대로 사용하는 함수

|ES6 함수의 구분|constructor|prototype|super|arguments|
|------|---|---|---|---|
|일반 함수|O|O|X|O|
|메서드|X|X|O|O|
|화살표 함수|X|X|X|X|

## 메서드
- ES6 사양에서 메서드는 `축약` 표현으로 정의된 함수만을 의미한다.
- 메서드는 인스턴스를 생성할 수 없으므로 prototype 프로퍼티가 없고 프로토타입도 생성하지 않는다.
- 메서드는 자신을 바인딩한 객체를 가리키는 내부 슬롯 [[HomeObject]]를 갖는다. 
- 메서드가 아닌 함수는 `super 키워드를 사용할 수 없다.` 메서드가 아닌 함수는 내부 슬롯 [[HomeObject]]를 갖지 않기 때문이다. 
```js
const base = {
  name: 'Lee',
  sayhi() {
    return `Hi! ${this.name}`
  }
}

const derived = {
  __proto__: base,
  // 이 메서드는 [[HomeObject]]를 갖는다.
  // 이 메서드의 [[HomeObject]]는 derived를 가리키고
  // super는 sayHi의 [[HomeObject]]의 프로토타입인 base를 가리킨다. 
  sayhi() {
    return `${super.sayhi()}, how are you doing?`
  }
}

console.log(derived.sayHi()) // Hi Lee, how are you doing>
```
- 따라서 메서드를 정의할 때 프로퍼티 값으로 익명 함수를 표현식으로 할당하는 ES6 이전의 방식은 사용하지 않는 것이 좋다. 
```js
// ES6 이전 프로퍼티 값으로 익명 함수를 표현식으로 할당하는 메서드 정의 방식
var person = {
  name: "홍길동",
  greet: function() {
    console.log("안녕하세요, " + this.name + "입니다.");
  },
  farewell: function() {
    console.log("안녕히 가세요, " + this.name + "입니다.");
  }
};

person.greet();    // 출력: 안녕하세요, 홍길동입니다.
person.farewell(); // 출력: 안녕히 가세요, 홍길동입니다.
```

## 화살표 함수
- 콜백 함수 내부에서 this가 전역 객체를 가리키는 문제를 해결하기 위한 대안으로 유용하다. 
- 객체 리터럴을 반환하는 경우 소괄호로 감싸 주어야 한다.
```js
const create = (id, content) => ({id, content})

create(1,'javaScript') // {id: 1, content: javaScript}
```
- 화살표 함수도 즉시 실행 함수로 사용할 수 있다. 

### 화살표 함수와 일반 함수의 차이점
- 화살표 함수는 인스턴스를 생성할 수 없는 non-constructor다.
- 중복된 매개변수 이름을 선언할 수 없다. 
- 화살표 함수는 함수 자체의 this 바인딩을 갖지 않는다. 따라서 화살표 함수 내부에서 this를 참조하면 스코프 체인을 통해 사위 스코프의 this를 참조한다. 

무엇보다 가장 큰 차이는 `this`다. 
- 콜백 함수 내부의 this가 외부 함수의 this와 다르기 때문에 발생하는 문제를 해결하기 위해 의도적으로 설계되었다. 
- 화살표 함수를 사용하여 콜백 함수 내부의 this 문제를 해결할 수 있다.
- 화살표 함수는 함수 자체의 this 바인딩을 갖지 않는다. 따라서 화살표 함수 내부에서 this를 참조하면 상위 스코프의 this를 그대로 참조한다. 이를 `lexical this` 라고 한다. 이는 마치 렉시컬 스코프와 같이 화살표 함수의 this가 함수가 정의된 위치에 의해 결정된다는 것을 의미한다.
