function Avatar() {
  return (
    <img
      className="avatar"
      src="https://i.imgur.com/1bX5QH6.jpg"
      alt="Lin Lanying"
      width={100}
      height={100}
    />
  );
}

export default function Profile() {
  return (
    // 자식 컴포넌트인 Avatar 컴포넌트에 아무런 props도 전달하지 않았다.
    <Avatar />
  );
}
