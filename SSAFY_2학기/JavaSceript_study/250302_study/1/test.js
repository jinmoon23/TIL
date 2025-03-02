const Person = class MyClass {}

const me = new Person()

console.log(MyClass) // ReferenceError: MyClass is not defined

const you = new MyClass() // ReferenceError: MyClass is not defined

