# OOP_1

## 객체 지향 프로그래밍(OOP)
- OOP 이전에 절차 지향 프로그래밍이 있었다.
  - 코드의 순차적 흐름과 함수 호출에 의해 프로그램이 진행
  - 재사용에 대한 중요성이 낮은 방식
  - 하드웨어의 급격한 발전으로 crisis 발생 -> 문제를 해결할 수 있는 새로운 패러다임의 필요성 대두 -> OOP (하지만 **대조되는 개념은 아님!** 오히려 파이썬 내부단의 동작은 절차지향적이기도 하다. 즉, 절차지향 위에 다양한 기능을 얹어 **보완하는 개념**이라고 이해해야 한다.)
- 데이터를 중요하게 다루면서 객체에 속한 메서드를 활용.
  - 데이터와 메서드(함수)를 객체(class)로 묶어서 활용하기 시작함.
    - 클래스는 파이썬에서 **타입**을 표현하는 방법임
    - 클래스는 데이터와 기능(메서드)를 묶는 방법을 제공
    - 예를들어 `str1 = 'a'` 라고 할당한 경우 a라는 변수의 타입은 `str`임. 따라서 `str` 클래스의 다양한 메서드를 `str1`변수가 활용할 수 있는 것은 클래스를 활용한 단적인 예.
- **클래스로 만든 객체를 인스턴스라 부름**
  - 가수라는 클래스를 정의하고 아이류를 인스턴스라고 부를 수 있나? X -> 아이유는 가수라는 클래스의 인스턴스다? O
  - `'1' == str(1)` 파이썬 내부적으로는 완전히 동일한 과정임. 
  - `'hello'.upper()` -> 인스턴스.메서드()의 형태. 즉 OOP에선 함수보다 데이터가 더 중점적인 역할을 맡는다. 

## 클래스로 만들어진 객체 == 인스턴스
- `만들어진` -> 그래서 보통 클래스를 **청사진**이라고도 부른다.
- 클래스를 정의하는 경우는 `class MyClass:` -> PascalCase(==UpperCamelCase) 방식으로 작성

## 클래스의 기본 구조
- `__init__` : 객체(인스턴스)를 생성할 때 자동으로 호출되는 특별한 메서드. 생성자 메서드. 매직메서드
  - 객체(인스턴스)의 초기화(생성)을 담당
  - 이 메서드를 통해 객체(인스턴스)를 생성함과 동시에 필요한 초기값을 설정한다.
- 인스턴스 변수
  - 객체(인스턴스)마다 고유하게 가지는 변수
  - 아래 코드에서 클래스에 생성자 메서드를 설정했다면 클래스의 인스턴스가 생성될 때 name 인스턴스 변수가 자동으로 생성된다.
```py
def __init__(self, name):
    self.name = name

singer_1 = Person('jinmoon')
```
- 클래스 변수
  - 클래스에 설정된 속성(변수)
- 인스턴스 메서드
  - 인스턴스가 가지는 메서드

## 클래스 변수와 인스턴스 변수
- 인스턴스의 변수(속성)을 변경한다고 클래스 변수(속성)이 변하지는 않는다. 즉, 인스턴스는 클래스의 변수에 접근은 할 수 있지만 값을 변경할수는 없다.  
- 이해를 위한 코드
```py
class Circle:
    pi = 3.14

    def __init__(self, r):
        self.r = r

c1 = Circle(5)
c2 = Circle(10)

print(c1.r) # 5
print(c2.r) # 10
print(c1.pi) # 3.14
c1.pi = 100 # Circle 클래스의 pi의 값을 수정한 것이 아니라 c1 인스턴스에 pi 변수를 생성한 것임
print(Circle.pi)
print(c1.pi) # 100
print(c2.pi) # 3.14
```

## 메서드에 대한 자세한 내용
- 인스턴스 메서드
  - `self` -> 인스턴스 메서드의 첫번째 인자는 반드시 자기 자신이어야 정상동작한다. 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적인 **표현**임 
    ```py
    'hello'.upper() == str.upper('hello')
    ``` 
    ```py
    class Person:
        def __init__(self,name):
            # 왼쪽 name : 인스턴스의 변수명
            # 오른쪽 name : 메서드의 매개변수
            self.name = name
            print('인스턴스가 생성되었습니다.')

        def greeting(self):
            print(f'안녕하세요 {self.name}입니다.') # self == instance

    person1 = Person('jimmoon') 
    person1.greeting() # 파이썬이 이해하는 것 -> Person.greeting(person1)
    Person.greeting(person1) # 위와 동일, 정상동작
    ```

- 클래스 메서드
  - `@classmethod`를 사용하여 정의 -> 함수를 꾸미는 함수
  - 클래스가 호출하는 메서드 -> 상속이라는 개념을 위한 메서드
  ```py
  class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def number_of_calculation(cls): 
        print(f'인구수는 {cls.count}입니다.') # ccls라고 설정되어 있지만 정의단에서는 'cls를 모른다' 라고 해야 맞다. 상속이라는 개념을 정상적으로 활용하기 위한 메서드

    person1 = Person('iu')
    person2 = Person('BTS')

    Person.number_of_calculation() # 이 순간에 cls 인자가 Person으로 결정됨
    ```
- 스태틱(정적) 메서드
  - 클래스 및 인스턴스와 상관없이 독립적으로 동작하는 메서드
  - `@staticmethod`를 사용하여 정의
  - 호출 시 필수적으로 작성해야 할 매개변수가 없음
    ```py
    class StringUtils:
        def __init__(self):
            pass
        
        @staticmethod
        def reverse_string(string):
            return string[::-1]
        
        @staticmethod
        def capitalize_string(string):
            return string.capitalize()

        text = 'hello, world'

        return1 = StringUtils.reverse_string(text)
        print(return1)

        return2 = StringUtils.capitalize_string(text)
        print(return2)
    ```

## 누가 어떤 메서드를 사용해야 하는가?
- 클래스 : 클래스 & 스태틱
- 인스턴스 : 인스턴스
```py
class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'


instance = MyClass()
# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance)) # 권장하지 않음
print(MyClass.class_method()) # 권장됨
print(MyClass.static_method()) # 권장됨

# 인스턴스가 할 수 있는 것
print(instance.instance_method()) # 권장됨
print(instance.class_method()) # 권장되지 않음
print(instance.static_method()) # 권장되지 않음
```

## 서로의 공간
- 인스턴스와 클래스 모두 각자의 공간(메모리)을 가짐
- 인스턴스에서 찾을 때 인스턴스 공간을 먼저 보고 클래스로 나아감
- 목적 : 클래스는 클래스 대로, 인스턴스는 인스턴스대로 각자 할 일에만 집중해! 만약 인스턴스에서 문제가 발생했어? 그럼 그거만 수정할게~

## 매직 메서드
- 특정 상황에 자동으로 호출되는메서드
- `__init__` / `__str__` 등
