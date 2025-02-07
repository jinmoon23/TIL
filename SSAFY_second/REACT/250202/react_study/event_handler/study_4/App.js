export default function LightSwitch() {
  function handleClick() {
    let bodyStyle = document.body.style;
    if (bodyStyle.backgroundColor === 'black') {
      bodyStyle.backgroundColor = 'white';
    } else {
      bodyStyle.backgroundColor = 'black';
    }
  }

  return (
    // evnetHandler에 전달되는 prop은 호출되는 것이 아니라 말 그대로 전달되는 것.
    // 따라서 ()를 붙이지 않아야 한다. 
    <button onClick={handleClick}>
      Toggle the lights
    </button>
  );
}
