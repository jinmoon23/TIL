export default function App() {
  return (
  // 1. 여러 개의 요소는 반드시 하나의 요소로 감싸야 함
  <>
    <h1>Hedy Lamarr's Todos</h1>
    <img
      src="https://i.imgur.com/yXOvdOSs.jpg"
      alt="Hedy Lamarr"
      class="photo"
    />
    <ul>
      {/* 2. 모든 태그는 닫아야 함 */}
        <li>Invent new traffic lights</li>
        <li>Rehearse a movie scene</li>
        <li>Improve the spectrum technology</li>
    </ul>
  </>
  );
}