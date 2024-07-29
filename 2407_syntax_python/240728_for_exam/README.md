# 파이썬 시험준비

## 문법 기초 
> 중요 키워드 및 문장 정리
1. sequence type -> **str**, list, range, **tuple**
   1. str과 tuple,range는 변경불가능한 sequence type
   2. sequence type이 가지는 순서는 정렬이 아님에 주의
2. nonsequence type -> set, dict
   1. 순서와 중복이 없는 변경 가능한 자료형
      1. 중복이 없다 -> key만 중복이 없으며 value는 중복이 있을 수 있다.
3. 명시적 형변환
   1. str -> int(float): 형식에 맞는 숫자만 가능
   2. int(float) -> str: 모두 가능
4. 비교연산자
   1. == : 동등성 
   2. is : 식별성
   3. is는 동일한 값과 동일한 메모리주소를 참조하는 것 까지 같아야 true를 반환함
    ```py
    a = [1, 2, 3]
    b = a  # b에 a를 할당하면 실제로 같은 객체를 가리키게 됨

    print(a is b)  # True, a와 b는 동일한 객체를 가리킴
    print(a == b)  # True, a와 b의 내용은 동일함

    c = [1, 2, 3]

    print(a is c)  # False, a와 c는 서로 다른 객체
    print(a == c)  # True, a와 c의 내용은 동일함
    ```
5. 시퀀스에서의 `+,*` 연산자
```py
# [1, 2, 'a', 'b']
print([1, 2] + ['a', 'b'])

# [1, 2, 1, 2]
print([1, 2] * 2)
```

## 함수
1. 위치인자
   1. 위치인자는 함수 호출 시 반드시 값을 명시해야 함.
2. 기본인자
   1. 함수 생성 시 매개변수에 기본값을 명시하는 것.
   2. 함수 호출 시 인자에 값을 할당하지 않으면 기본값이 적용됨.
   3. 기본인자를 설정하면 호출 시 반드시 인자에 값을 명시하지 않아도 됨.
3. 키워드인자
   1. 매개변수와 인자를 일치시키지 않고 순서를 마음대로하여 함수 호출이 가능.
   2. 하지만 키워드인자는 반드시 위치인자 뒤에 위치해야 정상동작함.
    ```py
    def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


    greet(name='Dave', age=35) # 안녕하세요, Dave님! 35살이시군요.
    greet(age=35, 'Dave')  #  positional argument follows keyword argument
    greet('Dave',age=35) # 정상동작하는 코드
    greet(age=29,name='jinmoon')
    ```
4. 임의의 인자 목록
   1. 함수 정의 시 매개변수 앞에 `*`키워드를 붙여 사용. 여러 개의 인자를 튜플로 사용.
5. 임의의 키워드 인자 목록
   1. 함수 정의 시 매개변수 앞에 ``**``키워드를 붙여 사용. 여러 개의 인자를 딕셔너리 형태로 사용.
6. 유용한 내장함수
   1. map(func,iter)
      1. 순회 가능한 모든 요소에 func를 적용하고 그 결과를 **map object**로 반환
    ```py
    numbers1 = input().split()
    print(numbers1)  # ['1,', '2,', '3']

    numbers2 = list(map(int, input().split()))
    print(numbers2)  # [1, 2, 3]

    numbers3 = map(int,input().split())
    print(numbers3) # map object
    ```
7. LEGB 룰 퀴즈
```python
a = 1
b = 2


def enclosed():
    a = 10
    c = 3

    def local(c):
        print(a, b, c) # 10 2 500

    local(500) # 2번째 실행, local 함수에 정의된 매개변수 c와 enclosed 함수에 포함된 변수 c는 아예 관계없음.
    print(a, b, c) # 3번째 실행, 10 2 3


enclosed() # 1번째 실행
print(a, b) # 4번째 실행, 1 2 
```

## 패킹과 언패킹
1. 패킹
   1. 여러 개의 값을 하나의 변수에 **튜플**의 형태로 담는다.
    ```python
    packed_values = 1, 2, 3, 4, 5
    print(packed_values)  # (1, 2, 3, 4, 5)
    ```
   2. *를 이용한 패킹
      1. 리스트로 패킹하여 할당
2. 언패킹
   1. 패킹된 변수의 값을 개별적인 변수로 분리하여 할당
    ```python
    packed_values = 1, 2, 3, 4, 5
    a, b, c, d, e = packed_values
    print(a, b, c, d, e)  # 1 2 3 4 5
    ```

## 흐름제어
1. if 조건문
   1. 복수조건문: 조건식을 동시에 검사하는 것이 아니라 순차적으로 검사
```py
dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
```
위 코드에서 480은 80보다도 크고 30보다도 크지만 print('나쁨')과 print('보통')이 실행되지 않는 이유는 아래와 같다.
> 파이썬에서 if, elif, else 구문은 조건이 만족되는 첫 번째 블록이  실행되면 그 이후의 블록들은 건너뛰게 됩니다. 이와 같은 논리 구조를 "단일 선택 구조"라고 합니다. 
> 
> 즉, if 블록에서 조건이 참이면 해당 블록이 실행되고, 다른 elif나 else 블록은 검사되지 않습니다. 따라서, dust = 480일 때 첫 번째 if 조건인 dust > 150이 참이기 때문에 그 블록 안에 있는 코드가 실행됩니다. 이어서 dust > 300 조건도 참이기 때문에 그 블록의 코드도 실행됩니다.
> 
>하지만 elif와 else 블록은 그 조건이 참이라도 실행되지 않습니다. 왜냐하면 if 블록에서 조건이 참으로 판명되어 이미 실행이 되었기 때문입니다.

2. 반복문
   1. for문: 임의의 시퀀스 내부의 항목을 시퀀스 **순서대로** 반복
      1. 반복가능한 시퀀스는 순서가 없는 시퀀스도 포함된다.(set,dict)
```py
    numbers = [4, 6, 10, -8, 5]
    
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    
    print(numbers) # [8, 12, 20, -16, 10]
```
리스트의 요소를 반복하는 것이 아닌 인덱스로 요소에 접근해 값을 변경하는 동작도 수행할 수 있다. 

## list comprehension
- 사용 전
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = []

    for num in numbers:
        squared_numbers.append(num**2)

    print(squared_numbers)  # [1, 4, 9, 16, 25]
    ```

- 사용 후
    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = [num**2 for num in numbers]
    # iter의 각 요소에 표현식의 연산을 수행하고 list로 감싸 해당 변수에 할당하라.

    print(squared_numbers)  # [1, 4, 9, 16, 25]

    result = [i for i in range(10) if i % 2 == 1]
    # 0~9까지의 iter의 각 요소 i는 조건문에 의해 결정되고 그 결정된 값을 리스트로 감싸 해당 변수에 할당하라.
    print(result)
    ```

## 클래스에 속한 다양한 메서드들
1. str
   1. capitalize(): 문장에서의 첫 단어만 대문자로 바꿈. title은 구분된 모든 단어의 첫 단어를 대문자로 바꿈.
    ```py
    print('helLO, WORLD, Day'.capitalize()) # Hello, world, day
    ```
    2. split(): 지정한 문자를 구분자로 해당 문자열을 분리하여 리스트로 반환. 구분자로 지정되었던 문자는 사라짐
    ```py
    'Hello, world'.split('o') # ['Hell', ', w', 'rld']
    ```
    3. **모든** 메서드는 이어서 사용가능
2. list
   1. remove()와 pop()의 차이점: 반환값이 있느냐 없느냐.
   2. sort()와 sorted()의 차이점
      1. sort()는 메서드 -> list의 원본을 수정하고 반환x
      2. sorted()는 내장함수 -> list의 사본을 반환
   3. 메서드 중 반환값이 있는 메서드: pop, index, count / 변경불가능한 값을 가지는 모든 데이터 타입의 메서드는 반환값이 항상 존재
3. set
   1. set의 pop()메서드는 list와 비슷하지만 순서가 없기때문에 인자를 받을 수 없다. 즉, set의 pop()메서드는 항상 임의의 값이 반환된다.
   2. set의 모든 집합 메서드는 반환값이 존재한다.
4. dict
   1. get(): 키와 연결된 값을 반환.(해당 키/값쌍을 제거하지는 않음)
      1. 만약 인자로 입력한 키가 딕셔너리에 없다면 기본값으로 None을 반환.
      2. None이 아닌 다른 값을 설정하면 해당값을 반환.
   2. pop(): 키/값쌍을 제거하고 그 값을 반환.
      1. 만약 인자로 입력한 키가 딕셔너리에 없다면 keyError가 발생
      2. 인자로 입력한 키가 없는 경우를 대비해 임의로 설정한 값을 인자로 전달하면 그 값을 반환함
   3. setdefault(): 키와 연결된 값을 반환.
      1. 만약 인자로 입력한 키/값쌍이 딕셔너리에 없다면 해당 키/값쌍을 딕셔너리에 추가하고 그 값을 반환.
      2. 만약 인자로 키만 전달했는데 그 키가 딕셔너리에 없다면 None을 반환. 하지만 get()과 달리 그 값이 딕셔너리에 추가됨.

## 클래스
1. 클래스 변수와 인스턴스 변수
    ```py
    class Circle:
        pi = 3.14

        def __init__(self, r):
            self.r = r 


    c1 = Circle(5)
    c2 = Circle(10)
    c2.pi = 5  # 인스턴스 변수 변경
    
    print(Circle.pi)  # 3.14 (클래스 변수)
    print(c1.pi)  # 3.14 (클래스 변수)
    print(c2.pi)  # 5 (새로운 인스턴스 변수가 생성됨)
    ```
2. 인스턴스 메서드의 self의 동작원리
```py
'hello'.upper() # 이 방식으로 우리는 흔히 메서드를 사용
str.upper('hello') # 파이썬 내부적으로 메서드가 동작하는 원리
# str 클래스의 upper 인스턴스 메서드를 실행하며 인자로 'hello'를 넣는다. 이것이 바로 인스턴스 메서드에서 항상 self를 첫번째 인자로 넘겨야 하는 이유. -> 객체 지향적 표현방식 
```

## 상속
1. 이유: 코드 재사용 / 계층 구조 / 유지보수의 용이성
2. 다중상속 시 중복된 속성이나 메서드가 있는 경우 **상속순서**에 의해 결정됨

## name space
1. 각 인스턴스는 독립적인 메모리공간을 가지며 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능함
2. OOP의 중요한 특성중 하나로 클래스와 인스턴스를 모듈화하여 각각의 객체가 독립적으로 동작하도록 보장한다.