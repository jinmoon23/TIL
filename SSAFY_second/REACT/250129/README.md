# react 초기설정 study

## SPA
1. 브라우저는 HTML 문서 하나를 적재한다.
2. 사용자는 사이트를 내비게이션 하지만 실제로는 하나의 페이지에 머무른다.
3. JS가 모든 처리를 대신한다. 

## REACT와 SPA
- REACT는 DOM을 갱신해주기 위해 만들어진 라이브러리
- 리액트 엘리먼트는 개념상 HTML 엘리먼트와 비슷하지만 실제로는 자바스크립트 객체(가상 DOM 개념)다.
- 다른식으로 말하자면 리액트 엘리먼트는 브라우저 DOM을 만드는 방법을 알려주는 명령이다. 
```js
React.createElement("h1", {id:"recipe-0"},"구운 연어")
// 위 코드(REACT 엘리먼트)는 아래의 HTML 엘리먼트를 생성하는 명령이다. 
<h1 id="recipe-0">구운 연어</h1>
// 아래의 코드는 REACT 엘리먼트를 나타낸다.
{
  $$typeof: Symbol(React.element),
  "type": "h1",
  "key": null,
  "ref": null,
  "props": {id: "recipe-0", children:"구운 연어"},
  "owner": null,
  "store": {}
}
``` 
