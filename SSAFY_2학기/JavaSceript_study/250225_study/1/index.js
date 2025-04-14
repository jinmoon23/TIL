const o = {}

// 모든 객체는 [[prototype]]이라는 내부 슬롯을 가짐.
console.log(o.__proto__)


const person = {
  name:'lee'
};

console.log(Object.getOwnPropertyDescriptor(person,'name'))