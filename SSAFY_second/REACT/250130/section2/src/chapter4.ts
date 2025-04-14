// Type Alias(타입 별칭 지정)
type User = {
  id: number;
  name: string;
  nickname: string;
  birth: string;
  bio: string;
  location: string;
};

// 여기서 객체의 타입을 지정할 때 미리 타입 별칭으로 만들어두었던 User 타입을 사용함.
let user: User = {
  id: 1,
  name: "이정환",
  nickname: "winterlood",
  birth: "1997.01.07",
  bio: "안녕하세요",
  location: "부천시",
};

let user2: User = {
  id: 2,
  name: "홍길동",
  nickname: "winterlood",
  birth: "1997.01.07",
  bio: "안녕하세요",
  location: "부천시",
};

// 인덱스 시그니쳐(Index Signature)
// 만약 이때 countryCodes에 100개의 프로퍼티(국가 코드)가 추가 되어야 한다면
// 타입 정의에도 각 프로퍼티를 모두 정의해주어야 하기 때문에 매우 불편할 것
type CountryCodes = {
  Korea: string;
  UnitedState: string;
  UnitedKingdom: string;
  // (... 약 100개의 국가)
  Brazil : string
};

let countryCodes: CountryCodes = {
  Korea: "ko",
  UnitedState: "us",
  UnitedKingdom: "uk",
  // (... 약 100개의 국가)
  Brazil : 'bz'
};

// 바로 이럴때 인덱스 시그니쳐를 이용하면 다음과 같이 간단하게 타입을 정의할 수 있음.
type CountryCodes2 = {
  // [key: string]은 CountryCodes2 타입의 프로퍼티 key가 문자열이고
  // 값도 문자열임을 의미
  [key: string]: string;
};

let countryCodes2: CountryCodes2 = {
  Korea: "ko",
  UnitedState: "us",
  UnitedKingdom: "uk",
  // (... 약 100개의 국가)
  Brazil : 'bz'
};