# study

## 리액트란?
사용자 인터페이스를 만들기 위한 JS 라이브러리

## 왜 주류가 되었는가?
- SPA(Single Page Application) 방식 적용
- 컴포넌트 기반 설계
  - 컴포넌트: 스스로 상태를 관리하는 캡슐화된 코드 조각
- 가상돔(Virtual DOM)
  - DOM: HTML 문서를 트리 구조로 표현해 각 태그(요소)를 객체로 다루도록 만든 것
  - DOM은 HTML로 작성된 웹페이지와 스크립트를 연결해 동적인 웹 환경을 만들도록 해주는 핵심 매개체
  - Virtual DOM: 실제 DOM과 동일한 구조를 지니지만 변경 사항을 적용할 때는 먼저 가상 DOM에서 수정한 뒤, 실제 DOM에는 변경된 부분만 최소한으로 반영하여 불필요한 작업을 줄이는 방식
  - 자주 변하는 UI를 효율적으로 다루고, 브라우저의 레이아웃 재계산과 리페인트 과정을 최소화하기 위해 Virtual DOM을 활용

## JSX란?
- JS + HTML
- 태그를 명시적으로 닫아줘야 하고 반드시 하나의 태그로 감싸져 있어야 동작한다. 
```js
import ReactDOM from 'react-dom';
// JSX의 문법 형식
const element = <h1>Hello, world!</h1>;

ReactDOM.render(
// 첫번째 인자를 두번째 인자의 요소에 렌더링하겠다.
  element,
  document.getElementById('root')
);
```

## JSX를 JS에서 사용하기
```js
let text = 'Hello, world!';
const num = 15;
const obj = { key: 0, a: 1, b: 2 };
const arr = ['a', 'b', 'c'];
const imageUrl =
  'https://dst6jalxvbuf5.cloudfront.net/static/img/logo/logo.svg';

const element = (
  <div>
    <h1>변수 넣기</h1>
    <ul>
    {/* 이런 방식으로 {}를 활용해 사용 */}
      <li>{text}</li>
      <li>{text + 'test'}</li>
    </ul>
    <h1>숫자 및 계산식 넣기</h1>
    <ul>
      <li>{num}</li>
      <li>{num + 15}</li>
    </ul>
```
- Object를 li 태그에 넣게되면 아래의 에러가 발생함. 이 경우에는 array를 사용하도록 하자.
```
Objects are not valid as a React child (found: object with keys {key, a, b}). If you meant to render a collection of children, use an array instead.
```
- JSX에는 IF문이 없다! 함수를 정의한 후 활용하는 편임. 
![JSX에서의 조건 표현](image.png)
```js
<div className={1 + 1 === 2 && "highlight"}>Hello3</div>
```
```
1 + 1 === 2는 참(true)이 되고, JavaScript에서 true && 'highlight'와 같은 논리연산은 왼쪽이 true면 오른쪽 값을 그대로 반환해요. 반면 왼쪽이 false면 오른쪽은 평가하지 않고 false를 반환하는 단축 평가(short-circuit evaluation) 방식이에요.
따라서 className={1 + 1 === 2 && 'highlight'}는 1 + 1 === 2 부분이 참이므로 결국 highlight 문자열이 최종 반환되어, 해당 엘리먼트가 class="highlight"를 갖게 돼요. 만약 1 + 1 === 3처럼 조건이 거짓이었다면 false가 반환되어 className이 적용되지 않아요.
```

## JSX에서의 반복문
- Key를 설정하는 것이 좋다! 이는 Vue와 동일한 듯.

## JSX에서의 스타일링
- 객체를 미리 객체로 코드블럭화한 후 간편하게 스타일 적용이 가능하다. 이 때 스타일 속성은 camelCase로 작성한다. 
```js
const roundBoxStyle = {
  position: 'absolute',
  top: 50,
  left: 50,
  width: '50%',
  height: '200px',
  padding: 20,
  background: 'rgba(162,216,235,0.6)',
  // 3. 속성은 camelCase
  borderRadius: 50
};
...
<div style={roundBoxStyle}>Hello1</div>
```

## JSX 실습
```js
const num = [1, 2, 3, 4, 5, 6, 7, 8, 9];

const element = (
  <div style={{ display: "flex" }}>
    {/* 여기에 JSX를 활용하여 요구사항에 맞게 구구단을 완성시켜보세요! */}
    {num.map((n) => {
      return (
        n !== 1 &&
        n !== 5 && (
          <div style={{ padding: 10, color: n % 2 ? "blue" : "black" }}>
            {num.map((m) => {
              return (
                <div>
                  {n} x {m} = {n * m}
                </div>
              );
            })}
          </div>
        )
      );
    })}
  </div>
);

ReactDOM.render(element, document.getElementById("root"));
```
![실습](image-1.png)

## JSX의 이해
- 자바스크립트 코드 안에서 마치 HTML을 작성하듯 태그 기반 문법을 사용할 수 있게 해주는 확장 문법
- React에서 JSX를 사용하면 UI 구조를 직관적으로 표현할 수 있고, 자바스크립트 로직과 UI를 한 파일에 담을 수 있어 코드 재사용성과 유지보수성을 높여줌
![JSX의 이해](image-2.png)