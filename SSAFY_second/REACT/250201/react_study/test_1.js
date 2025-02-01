function AdminPanel() {
  let content;
  if (isLoggedIn) {
    content = <AdminPanel />;
  } else {
    content = <LoginForm />;
  }
  return (
    <div>
      {content}
    </div>
  );
}


// 위 코드는 아래와 같이 삼항 연산자로 나타낼 수 있다.
// 아래의 방식이 더 간결하고 필요없는 변수를 선언하지 않아도 된다.

function AdminPanel() {
  return (
    <div>
      {isLoggedIn ? <AdminPanel /> : <LoginForm />}
    </div>
  );
}
