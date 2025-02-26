# 객체지향 프로그래밍
- 객체의 `상태`를 나타내는 데이터와 상태 데이터를 조작할 수 있는 `동작`을 하나의 논리적인 단위로 묶어 생각한다. 

## 프로토타입 객체
- 생성자 함수를 통해 많은 인스턴스 생성에 대응할 수 있지만 동일한 동작을 하는 메서드를 인스턴스 생성시 마다 생성할 필요는 없다. 이를 위해 JS는 프로토타입 객체를 통해 메서드 상속을 구현한다. 물론 프로퍼티도 상속받을 수 있다. 
```js
function Circle(radius) {
  this.radius = radius;
  Circle.prototype.getArea = function () {
    return Math.PI * this.radius **2;
  };
}
// 아래 두 인스턴스는 동일한 메서드 getArea를 공유한다. 
const circle1 = Circle(2)
const circle2 = Circle(5)
```
- 프로토타입은 어떤 객체의 상위(부모)객체의 역할을 하는 객체로서 다른 객체에 공유 프로퍼티(메서드 포함)를 제공한다. 