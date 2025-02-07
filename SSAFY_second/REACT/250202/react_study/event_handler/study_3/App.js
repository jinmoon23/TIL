export default function Toolbar() {
  return (
    <div className="Toolbar" onClick={() => {
      alert('You clicked on the toolbar!');
    }}>
      {/* toolbar 내부의 버튼을 클릭한 경우 */}
      {/* 해당 버튼에 대한 동작이 먼저 수행되고 */}
      {/* 이후 트리를 따라 위로 전파되어 동작들이 수행된다 */}
      <button onClick={() => alert('Playing!')}>
        Play Movie
      </button>
      <button onClick={() => alert('Uploading!')}>
        Upload Image
      </button>
    </div>
  );
}
