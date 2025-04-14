# study

## 컴포넌트
스스로 상태를 관리하는 캡슐화된 코드 조각 === 하나의 JSX를 반환하는 함수

```js
import Hello from "./hello";
import World from "./world";
// export를 통해 다른 .js 파일에서 아래의 함수를 import 할 수 있다.
export default function App() {
  return (
    <div>
      {/* 태그 내부에 값이 들어가지 않기 때문에 단축표현이 가능 */}
      <Hello />
      <World />
    </div>
  );
}

export default function Hello() {
  return <h1>Hello</h1>;
}

export default function World() {
  return <h2>World</h2>;
}
```
- 컴포넌트의 함수는 `PascalCase`를 적용
- 컴포넌트는 `의미 단위`로 쪼개서 파일을 분리한다. 

## Props(Properties의 줄임말)
- 부모 컴포넌트에서 자식 컴포넌트로 내려주는 데이터
- Props 활용 팁
  - `구조분해할당`을 잘 활용하자
  - 특정 Props에 `기본 값`을 줄 수 있다.
  - Props는 `읽기 전용`이다.
```js
export default function Heading(props) {
  // type은 식별하기 위한 이름으로 이해해도 무방할 듯.
  // 여기서 컴포넌트 정의 후 아래의 App() 함수에서 호출되어 최종적으로 JSX를 리턴한다. 
  if (props.type === "h2") {
    return <h2>{props.children}</h2>;
  }
  return <h1>{props.children}</h1>;
}

import Heading from "./components/Heading";
export default function App() {
  return (
    <div>
      <Heading type="h1">Hello</Heading>
      <Heading type="h2">World</Heading>
    </div>
  );
}
```

## State
- 컴포넌트 내부에서 사용되는 변수
- State 값이 변하면 컴포넌트가 리렌더링 됨.
- 렌더링 사이클에서 값이 보전됨.
```js
// - value를 state로 만들기
// - Increase 버튼 함수 만들기 (+함수형 인자로)
// - Reset 버튼 함수 만들기

import { useState } from "react";

export default function App() {
  const [value, setValue] = useState(0);

  return (
    <div>
      <h1>value: {value}</h1>
      <button
      {/* React JSX 문법에서는 중괄호({})를 사용해 자바스크립트 표현식을 태그 안에 직접 삽입할 수 있다.  */}
        onClick={() => {
          console.log("Increase value1", value);
          // setter 함수
          setValue(value + 1);
          console.log("Increase value2", value);
        }}
      >
        Increase value
      </button>
      <button
        onClick={() => {
          setValue(0);
        }}
      >
        Reset value
      </button>
    </div>
  );
}
```

## 클래스형 컴포넌트
- 레거시로 남아있지만 지금은 Hooks가 완전히 정착하여 기본형으로 사용됨.

## URL에서 컴포넌트 HTML을 받아와 Props 실습하기
```js
// App.js
import CourseCard from "./components/CourseCard";

function App() {
  return (
    <div style={{ padding: 30 }}>
      <CourseCard
        img="https://dst6jalxvbuf5.cloudfront.net/media/images/Course/cover_image/210909_191531/23.png"
        tags={["발표", "패키지", "최대할인"]}
        title="비즈니스 올인원, 방구석 어학연수 패키지"
        startPrice={349000}
        types={["동영상 강의"]}
      />
    </div>
  );
}

export default App;

// CourseCard.js
import "./CourseCard.css";

function CourseCard({ img, tags, title, startPrice, types }) {
  return (
    <div className="course-card col-sm-6 col-md-4 col-lg-3">
      <div className="cover">
        <img src={img} />
      </div>
      <div className="info">
        <ul className="tags">
          {tags.map((item, i) => {
            return (
              <li key={i} class="tag">
                {item}
              </li>
            );
          })}
        </ul>
        <h4 className="name">{title}</h4>
        <div className="price">{startPrice.toLocaleString()}원부터</div>
      </div>
      <ul className="types">
        {types.map((item, i) => {
          return (
            <li key={i} class="type">
              {item}
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default CourseCard;

```
![Props 실습](image.png)

## Hooks를 통한 동작 기반 이해하기
- useEffect(vue3의 `watch`와 유사)
```
  //  useEffect: 컴포넌트가 렌더링 될 때, 특정 작업을 실행
  //  - 인자
  //    - 실행하고자 하는 함수 (effect callback)
  //      - effect는 정리(clean-up) 함수를 반환할 수 있음
  //      - 반환된 함수는 컴포넌트가 언마운트 또는 effect 재실행 이전에 실행됨
  //    - 의존성 배열 (dependency list) -> 해당 value가 변할때 마다 재렌더링
```

