export default function Clock({ time }) {
  let hours = time.getHours();
  // dom을 직접 조작하는 것은 사이드 이펙트에 해당하여 순수함수로의 요건을 지키지 못한다.
  // 따라서 아래와 같이 간접 조작으로 순수함수의 요건을 지킬 수 있다. 
  let className = hours >= 0 && hours <= 6 ? "night" : "day"
  return (
    <h1 id="time" className={className}>
      {time.toLocaleTimeString()}
    </h1>
  );
}
