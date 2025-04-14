// 선택적 프로퍼티 연습

let user: {
  id: number;
  name: string;
} = {
  id: 1,
  name: "이정환",
};

user = {
  name: "홍길동", // 오류 발생!
};

// 이렇게 특정 프로퍼티를 상황에 따라 생략하도록 만들고 싶다면
// 해당 프로퍼티를 선택적 프로퍼티로 만들어줘야 합니다.

let user2: {
  id?: number; // 선택적 프로퍼티가 된 id
  name: string;
} = {
  id: 1,
  name: "이정환",
};

user2 = {
  id: "id", // 오류 발생! value 타입은 반드시 number 타입이어야 한다
  name: "홍길동",
};

// 읽기전용 프로퍼티 연습

let user3: {
  id?: number;
  readonly name: string; // name은 이제 Readonly 프로퍼티가 되었음
} = {
  id: 1,
  name: "이정환",
};

user.name = "dskfd"; // 오류 발생
// 읽기 전용 프로퍼티를 활용해 객체의 일부 프로퍼티만 수정할 수 있도록 할 수 있음.