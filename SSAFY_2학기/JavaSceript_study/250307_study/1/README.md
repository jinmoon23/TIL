> 얕은 복사와 깊은 복사
- 객체를 프로퍼티 값으로 갖는 객체의 경우 얕은 복사는 한 단계까지만 복사하는 것을 말하고 깊은 복사는 객체에 중첩되어 있는 객체까지 모두 복사하는 것을 말한다. 
- BuiltIn 메서드는 모두 얕은 복사를 수행한다. 따라서 깊은 복사가 필요한 경우 `Lodash` 라이브러리의 cloneDeep 메서드를 사용하는 것을 추천.

> 유사 배열 객체
- 배열처럼 보이는 객체로, 숫자형 인덱스와 `length` 프로퍼티를 가지고 있지만 실제 배열은 아닌 객체를 의미.
- 유사 배열 객체는 실제 배열이 아니므로 `forEach`, `map`, `filter` 같은 배열 메서드를 직접 사용할 수 없습니다.
따라서 `Array.from()` 메서드를 사용해 `유사 배열 객체를 배열로 변환`하여 유용한 배열 메서드를 활용할 수 있습니다.
```js
function sum () {
  const arr = Array.from(arguments)
  console.log(arr)

  return arr.reduce((pre,cur) => pre + cur, 0)
}

console.log(sum(1,2,3)) // 6
```
- 위 코드블럭에서 arguments 객체는 유사 배열 객체이다. `Spread 문법`을 통해 더 간단하게 배열로 변환할 수 있다. 

```js
function sum() {
  const arr = [...arguments]
  console.log(arr)

  return arr.reduce((pre,cur) => pre + cur, 0)
}

console.log(sum(1,2,3)) // 6
```

## Array.prototype.join

> 해당 메서드는 원본 배열의 모든 요소를 `문자열`로 변환한 후, 인수로 전달받은 `문자열`, 즉 구분자로 연결한 `문자열을 반환`한다. 

## Array.prototype.reverse
 > `원본 배열`의 순서를 반대로 뒤집어 반환한다. 이때 원본 배열이 변경된다. 즉, 부수효과가 있는 메서드다.

## Array.prototype.fill
> 인수로 전달받은 값을 배열의 처음부터 끝까지 요소로 채운다. 이때 원본 배열이 변경된다. 즉, 부수효과가 있는 메서드다. 
- 두 번째 인자로 요소 채우기를 시작할 인덱스를 전달할 수 있다.
- 세 번째 인자로 요소 채우기를 그만둘 인덱스를 전달할 수 있다. 

> Array.from 메서드를 사용하면 두 번째 인수로 전달한 콜백 함수를 통해 요소값을 만들면서 배열을 채울 수 있다. 

```js
// 아래 코드에서 {length}는 길이만 정의된 유사 배열 객체를 전달하는 코드임.
const sequence = (length = 0) => Array.from({length}, (_, i) => i)

console.log(sequence(3)) // [0,1,2]
```
- 위 코드블럭에서 `Array.from({length}, (_, i) => i)`의 세부 동작 과정과 원리는 다음과 같다. 
1. `{length}`는 호출될 때 length 프로퍼티의 값이 정해진다. 위 코드블럭에선 3이다.
2. 1에 의해 생성된 유사 배열 객체는 length 프로퍼티만 가지고 인덱스로 접근해 값을 확인해봐도 `undefined`다. 즉, `sequence[0] === undefined` 인 것.
3. Array.from() 메서드의 두 번째 인자는 첫 번째 인자인 배열 혹은 유사 배열 객체의 각 요소에 대한 동작을 가지는 콜백 함수를 받는다.
4. 유사 배열 객체의 length 프로퍼티 값은 3이기 때문에 3번의 순회를 통해 0,1,2를 반환하고, 반환된 값은 유사 배열 객체의 각 요소 값으로 치환된다. 
5. 이상의 모든 과정은 Python의 `sequence = list(range(3))`과 정확히 일치한다. 