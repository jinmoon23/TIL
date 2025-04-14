# 객체 리터럴의 간편한 표현들
```js
var x = 1, y = 2;

var obj = {
  x:x,
  y:y
};
console.log(obj) // {x:1, y:2}
```
- 프로퍼티 값으로 변수를 사용하는 경우 변수 이름과 프로퍼티 키가 동일한 이름일 때 프로퍼티 키를 생략할 수 있다.

```js
let x = 1, y = 2;

const obj = {x, y}

console.log(obj) // {x:1, y:2}
```

