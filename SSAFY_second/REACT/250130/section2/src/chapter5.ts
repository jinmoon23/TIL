// enum 타입
// js에는 존재하지 않고 ts에서만 지원하는 타입
// enum의 각 멤버에는 다음과 같이 숫자를 할당할 수 있습니다. 
enum Role {
  // 만약 값을 할당하지 않으면 0부터 시작해서 1씩 증가한 값을 각 멤버에 할당합니다.
  ADMIN = 0,
  USER = 1,
  GUEST = 2,
}
// enum의 멤버들을 값으로도 활용 할 수 있습니다.
const user1 = {
  name: "이정환",
  role: Role.ADMIN, //관리자
};

const user2 = {
  name: "홍길동",
  role: Role.USER, // 회원
};

const user3 = {
  name: "아무개",
  role: Role.GUEST, // 게스트
};

// enum은 컴파일 시 다른 타입들 처럼 사라지지 않고 객체로 남아있기 때문에
// enum의 멤버들을 값으로 활용할 때 유용합니다.
// tsc 명령어로 컴파일된 js 파일을 확인해보면 enum이 객체로 남아있는 것을 확인할 수 있습니다.