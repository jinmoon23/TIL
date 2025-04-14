// 객체 타입의 호환성

type Animal = {
    name: string;
    color: string;
  };
  
  type Dog = {
    name: string;
    color: string;
    breed: string;
  };
  
  let animal: Animal = {
    name: "기린",
    color: "yellow",
  };
  
  let dog: Dog = {
    name: "돌돌이",
    color: "brown",
    breed: "진도",
  };
// animal 타입이 dog 타입에 비해 슈퍼 타입이다. 
  animal = dog; // ✅ OK
  dog = animal; // ❌ NO

// 위 코드에서 dog 객체는 Animal 타입의 객체에 할당할 수 있지만, animal 객체는 Dog 타입의 객체에 할당할 수 없다.
// 이는 Animal 타입의 객체가 Dog 타입의 객체보다 더 일반적이기 때문이다.
// 타입스크립트는 프로퍼티를 기준으로 타입을 정의하는 구조적 타입 시스템을 따른다고 배웠던 적 있습니다. 
// 따라서 Animal 타입은 name과 color 프로퍼티를 갖는 모든 객체들을 포함하는 집합으로 볼 수 있고 
// Dog 타입은 name과 color 거기에다 추가로 breed 프로퍼티를 갖는 모든 객체를 포함하는 집합으로 볼 수 있습니다.
// 그러므로 어떤 객체가 Dog 타입에 포함된다면 무조건 Animal 타입에도 포함됩니다.
// 그러나 반대로 Animal 타입에 포함되는 모든 객체가 Dog 타입에 포함되는것은 아닙니다. 