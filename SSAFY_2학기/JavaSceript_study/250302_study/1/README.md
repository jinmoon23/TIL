# 클로저

- 함수와 그 함수가 정의된 렉시컬 환경과의 조합이다.

```js
const x = 1;

function foo() {
  const x = 10;
  bar();
}

function bar() {
  console.log(x);
}

foo(); // 1
bar(); // 1
```

- 상위 스코프에 대한 참조는 함수 `정의`가 평가되는 시점에 함수가 정의된 환경(위치)에 의해 결정된다. 이것이 바로 렉시컬 스코프의 전부다.
- 외부 함수보다 중첩 함수가 더 오래 유지되는 경우 중첩 함수는 이미 생명 주기가 종료한 외부 함수의 변수를 참조할 수 있다. 이러한 중첩 함수를 클로저라고 부른다.

```js
const x = 1;

function outer() {
  const x = 10;
  const inner = function () {
    console.log(x);
  };
  return inner;
}
// outer 함수 호출과 함께 함수 내부의 동작이 이루어진 후 x 변수는 생명 주기를 마감함
const innerFunc = outer();
// 그럼에도 불구하고 x 변수에 접근할 수 있는 이유는 실행 컨텍스트 스택에서 outer 함수가 제거되지만
// outer 함수의 렉시컬 환경까지 소멸하는 것은 아니기 때문.
innerFunc(); // 10
```

- 위 예제에서 inner 함수는 전역 변수 innerFunc에 의해 참조되고 있으므로 가비지 컬렉션의 대상이 되지 않는다.
- js의 모든 함수는 상위 스코프를 기억하므로 이론적으로 모든 함수는 클로저다. 하지만 상위 스코프의 어떤 식별자도 참조하지 않는 중첩 함수는 클로저가 아니다. 참조하지도 않는 식별자를 기억하는 것은 메모리 낭비이기 때문.
- 또한 외부 함수보다 생명 주기가 짧은 경우 중첩 함수가 반환되지 않기 때문에 클로저라고 볼 수 없다. 이는 생명 주기가 종료된 외부 함수의 식별자를 참조할 수 있다는 클로저의 본질에 부합하지 않기 때문.
- 이처럼 클로저는 중첩 함수가 상위 스코프의 식별자를 참조하고 있고 중첩 함수가 외부 함수보다 더 오래 유지되는 경우로 한정하는 것이 일반적이다.

## 클로저에 의해 참조되는 변수 = 자유변수

- 클로저란 `함수가 자유 변수에 대해 닫혀있다` 라는 의미다. === `자유 변수에 묶여있는 함수`

## 클로저의 유용성

- 상태를 안전하게 변경하고 유지하기 위해 사용한다. 이는 상태를 안전하게 은닉하고 특정 함수에게만 상태 변경을 허용하기 위해 사용할 수 있다는 의미.

```js
let num = 0;

const increase = function () {
  return ++num;
};
```

- 위 코드는 잘 동작하지만 num 변수가 전역에 선언되었기 때문에 increase 함수가 호출되지 전까지 계속해서 변경되지 않은 상태를 유지해야 한다는 조건을 충족하기 힘들다는 문제 가능성을 내포하고 있다.

```js
const increase = (function () {
  let num = 0;

  return function () {
    return ++num;
  };
})();
console.log(increase()); // 1
console.log(increase()); // 2
console.log(increase()); // 3
```

- 위 예제의 동작 과정은 아래와 같다.

1. 위 코드가 실행되면 외부 함수인 즉시 실행 함수가 동작하고 increase 변수에는 클로저가 할당된다.
2. 클로저는 상위 스코프를 기억하고 자유 변수인 num을 언제 어디서든 어떤 방식으로도 참조할 수 있다.
3. 즉시 실행 함수는 한 번만 실행되므로 increase 함수가 호출될 때마다 num 변수가 재차 초기화될 일은 없을 것이다.

이를 좀 더 확장하면 아래의 코드를 작성할 수 있다.

```js
const counter = (function () {
  let counter = 0;

  return function (f) {
    counter = f(counter);
    return counter;
  };
})();

function increase(n) {
  return ++n;
}

function decrease(n) {
  return --n;
}

console.log(counter(increase)); // 1
console.log(counter(increase)); // 2

console.log(counter(decrease)); // 1
console.log(counter(decrease)); // 0
```

# 클래스

- 클래스와 생성자 함수는 모두 프로토타입 기반의 인스턴스를 생성하지만 정확히 동일하게 동작하지는 않는다.
- 클래스는 함수다. 따라서 값처럼 사용할 수 있는 일급 객체다.
- 클래스는 인스턴스를 생성하는 것이 유일한 존재 이유이므로 반드시 `new` 연산자와 함께 호출해야 한다.

## 클래스의 메서드

- constructor 메서드: 인스턴스를 생성하고 초기화하기 위한 특수한 메서드.
  - constructor 내부의 this는 생성자 함수와 마찬가지로 클래스가 생성한 인스턴스를 가리킨다.
  - constructor는 클래스 내에 최대 한 개만 존재할 수 있다.
  - constructor는 생략할 수 있다.
  - constructor는 별도의 반환문을 갖지 않아야 한다. 만약 this가 아닌 다른 객체를 명시적으로 반환하면 this, 즉 인스턴스가 반환되지 못하고 return 문에 명시한 객체가 반환된다.
  - 하지만 만약 원시값을 반환하면 원시값 반환은 무시되고 암묵적으로 this가 반환된다.
- 프로토타입 메서드: 클래스 몸체에서 정의한 메서드는 생성자 함수에 의한 객체 생성 방식과는 다르게 클래스의 prototype 프로퍼티에 메서드를 추가하지 않아도 `기본적으로` 프로토타입 메서드가 된다.
- 정적 메서드: `static` 키워드를 붙이면 정적 메서드(클래스 메서드)가 된다.

## 정적(클래스) 메서드와 프로토타입 메서드

- 메서드 내부에서 인스턴스 메서드를 참조할 필요가 있다면 this를 사용해야 하며, 이러한 경우 프로토타입 메서드를 정의해야 한다. 하지만 메서드 내부에서 인스턴스 프로퍼티를 참조해야 할 필요가 없다면 정적(클래스) 메서드를 사용하는 것이 좋다.

## 클래스의 프로퍼티

- 인스턴스 프로퍼티: constructor 내부에서 정의해야 한다.

## 클래스의 private 필드 정의

- 클래스도 생성자 함수와 마찬가지로 다른 클래스 기반 객체지향 언어에서는 지원하는 private, public, protected 키워드와 같은 접근 제한자를 지원하지 않는다. 다만 js의 상위 확장자인 ts는 완벽하게 지원한다.
- 또한 chrome 74 이상과 node 12 이상부터는 private 필드에 대한 기능이 구현되어 있다.

```js
class Person {
  // private 변수 선언
  #name = "";

  constructor(name) {
    this.#name = name;
  }
}
const me = new Person("Choi");

console.log(me.#name); // 클래스 외부에서 참조할 수 없음
```

- 위의 private 필드는 반드시 클래스 몸체에 선언해야지 에러가 발생하지 않는다. constructor에 정의하면 안됨!

## 상속에 의한 클래스의 확장

- 프로토타입 기반 상속은 프로토타입 체인을 통해 다른 객체의 자산을 상속받는 개념이지만 상속에 의한 클래스의 확장은 기존 클래스를 상속받아 새로운 클래스를 확장하여 정의하는 것이다.

## extends 키워드를 사용한 클래스 정의

- 수퍼클래스와 서브클래스는 인스턴스의 프로토타입 체인뿐 아니라 클래스 간의 프로토타입 체인도 생성한다. 이를 통해 프로토타입의 메서드, 정적 메서드 모두 상속이 가능하다.

## super 키워드

- 함수처럼 호출할 수도 있고 this와 같이 식별자처럼 참조할 수 있는 특수한 키워드다.
  - super를 `호출`하면 수퍼클래스의 `constructor`를 호출한다.
  - super를 `참조`하면 수퍼클래스의 `메서드를 호출`할 수 있다.

```js
// super 호출을 통한 constructor 호출의 적절한 용례
class Base {
  constructor(a, b) {
    this.a = a;
    this.b = b;
  }
}

class Derived extends Base {
  constructor (a,b,c) {
    super(a,b)
    this.c = c
  }
}

const derived = new Derived(1,2,3)
console.log(derived) // Derived {a:1, b:2, c:3}
```

```js
// super 참조를 통한 수퍼클래스의 메서드 호출의 용례

class Base {
  constructor (name) {
    this.name = name
  }
  
  sayHi () {
    return `Hi! ${this.name}`
  }
}

class Derived extends Base {
  sayHi () {
    return `${super.sayHi()}. how are you doing?`
  }
}

const derived = new Derived('Choi')
console.log(derived.sayHi()) // Hi! Choi. how are you doing?
```

## 상속 클래스의 인스턴스 생성 과정