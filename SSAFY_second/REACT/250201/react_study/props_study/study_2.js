// Avatar 컴포넌트는 부모 컴포넌트에게서 받은 props를 사용한다.
// 이러한 방식으로 컴포넌트 간에 데이터를 전달할 수 있다.
// person 객체의 이름은 동일하게 하는것이 관례
// 아래 코드의 {person, size}는 props를 구조분해할당하여 받은 것이다.
function Avatar({ person, size }) {
  return (
    <img
      className="avatar"
      src={getImageUrl(person)}
      alt={person.name}
      width={size}
      height={size}
    />
  );
}
// props는 함수의 인수와 동일한 역할을 한다.
// 사실 props는 컴포넌트에 대한 유일한 인자임
// 따라서 아래와 같이 코드를 작성할 수 있다.
function Avatar(props) {
  let person = props.person;
  let size = props.size;
  return (
    <img
      className="avatar"
      src={getImageUrl(person)}
      alt={person.name}
      width={size}
      height={size}
    />
  );
}

export default function Profile() {
  return (
    <Avatar
      person={{ name: 'Lin Lanying', imageId: '1bX5QH6' }}
      size={100}
    />
  );
}