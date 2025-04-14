// any 타입
// any 타입은 타입스크립트에서만 제공되는 특별한 타입으로 
// 타입 검사를 받지 않는 특수한 치트키 타입
let anyVar: any = 10;
anyVar = "hello";

anyVar = true;
anyVar = {};

anyVar.toUpperCase();
anyVar.toFixed();
anyVar.a;
// any 타입은 타입 검사를 받지 않는 타입이므로 
// 모든 타입스크립트의 문법과 규칙으로부터 자유롭지만 그만큼 위험한 타입
// 정말 어쩔 수 없는 경우를 제외하고는 any 타입을 사용하지 않는것을 강력히 권장

// unknown 타입
// any 타입과 마찬가지로 모든 타입을 허용하는 타입이지만
// any 타입과는 다르게 unknown 타입은 타입 검사를 받는 타입
// 따라서 보다 안전한 타입이다.

let num: number = 10;
// 아래에서 보듯 unknown 타입에는 어떤 값이든 저장할 수 있지만
let unknownVar: unknown;
unknownVar = "";
unknownVar = 1;
unknownVar = () => {};
// 반대로 number 타입에는 unknown 타입을 저장할 수 없다.
num = unknownVar; // 오류 !

// unknown 타입의 값은 어떤 연산에도 참여할 수 없으며, 
// 어떤 메서드도 사용할 수 없습니다.
// 쉽게 정리하면 unknown 타입은 오직 값을 저장하는 행위밖에 할 수 없게 됩니다.
unknownVar * 2 // 오류 !

// 따라서 특정 변수가 당장 어떤 값을 받게 될 지 모른다면 
// any 타입으로 정의하는 것 보단 unknown 타입을 이용하는게 
// 훨씬 안전한 선택이 됩니다.