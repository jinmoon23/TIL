// hook 사용하기
// 컴포넌트 간에 데이터 공유하기

import { useState } from 'react';

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}

// 위 코드에서 아래의 코드로 변경하면
// 두 버튼이 같은 카운터를 공유하게 된다.
// 이를 해결하기 위해 props를 사용한다.

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }
// 각 버튼의 onClick prop은 MyApp 내부의 handleClick 함수로 설정되었으므로 
// 그 안에 있는 코드가 실행됩니다. 이 코드는 setCount(count + 1)를 실행하여 
// count state 변수를 증가시킵니다. 
// 새로운 count 값은 각 버튼에 prop으로 전달되므로 모든 버튼에는 새로운 값이 표시됩니다. 
// 이를 "state lifting"이라고 합니다.
  return (
    <div>
      <h1>Counters that update separately</h1>
      {/* 이렇게 전달한 정보를 props 라고 함 */}
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({count, onClick}) {
  // 여기 있던 코드가 위로 올라감

  return (
    <button onClick={onClick}>
      Clicked {count} times
    </button>
  );
}