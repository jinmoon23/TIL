# Function & 제어문

# function
- 특정 동작 재사용을 위한 코드 묶음
- 프린트 함수의 리턴값은 None임! 프린트(출력)과 리턴은 다름을 인식하자!
```python
def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2

result = make_sum(1,100)
return_value = print(result)
print(return_value)
```

```python
def my_func():
    print('hello') # hello

result = my_func()
print(result) # None
```
- 매개변수와 인자
  - 매개변수: 함수가 **받을 값**을 나타내는 변수
  - 인자: 함수로 **전달되는 값**
  - 결론: 다항식을 생각해보자 y = x - 3, 여기서 x,y를 매개변수라고 하고 임의로 넣는 값을 인자라고 이해하면 됨

- 위치인자
  - 기본적으로 만드는 함수의 형태, 매개변수에 설정한 매개변수를 호출 시 인자로 설정하지 않으면 타입에러가 발생함
```python
# 1. Positional Arguments
def greet(name,age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('진문','20')
greet('20','진문')
```
- 기본 인자 값
  - 매개변수에 기본값을 설정
  - 더 유연한 함수 활용이 가능함
```python
def greet(name,age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet('진문')
greet('진문','40')
```

- 키워드 인자 값
```python
def greet(name,age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')

greet(name='진문',age=20)
greet(age=35,name='석호')
greet(age=15,'진호') # 오류 발생
```
- 임의의 인자 목록
  - 정해지지 않은 개수의 인자를 처리하는 인자
  - 매개변수 앞에 *를 붙여 사용, 여러 개의 인자를 튜플로 처리.
```python
def calculate_sum(*args):
    print(args)
calculate_sum(1,3,100)
```
- 임의의 키워드 인자 목록
  - 정해지지 않은 개수의 키워드 인자를 처리하는 매개변수 설정
  - 여려 개의 인자를 딕셔너리로 묶어 처리

- 함수 인자 권장 작성순서
  - 위치 -> 기본 -> 가변 -> 가변 키워드, 단 상황에 따라 유연하게 적용

## 재귀 함수
- 자기 자신을 호출하는 함수
```python
def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)

# 팩토리얼 계산 예시
print(factorial(5))  # 120
# 5 x f(4)
# 4 x f(3)
# 3 x f(2)
# 2 x f(1)
# 1 -> 5 x 4 x 3 x 2 x 1
```

## 내장 함수

- 유용한 내장 함수
  - map(): 2개의 인자를 받는다. (함수, 순회 가능한 요소), 순회 가능한 요소는 컬렉션을 의미.
  - 마치 **반복문** 처럼 사용되는 함수!
```python
# map()의 활용
numbers1 = input().split()
print(numbers1)  # ['1', '2', '3']

numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]
```
  - zip(): (*순회 가능한 요소), 순회 가능한 요소를 모아 tuple 리턴
```python
girls = ['jane', 'ashley']
boys = ['peter', 'jay']
pair = zip(girls, boys)
print(pair)  # <zip object at 0x000001C76DE58700>
print(list(pair))  # [('jane', 'peter'), ('ashley', 'jay')], 인덱스 동일!

kr_scores = [10, 20, 30, 50]
math_scores = [20, 40, 50, 70]
en_scores = [40, 20, 30, 50]

for student_scores in zip(kr_scores, math_scores, en_scores):
    print(student_scores)   

scores = [
    [10, 20, 30],
    [40, 50, 39],
    [20, 40, 50],
]
for score in zip(*scores):
    print(score)
```

## 함수와 scope
- LEGB Rules : 파이썬 인터프리터는 깊은 곳에서 얕은 곳의 방향으로 변수를 찾아감! 그래서 내장함수에 해당하는 이름의 변수를 깊은 곳에서 할당하면 그 이후로는 해당 내장함수를 사용하지 못함
- 테스트
```python
a = 1
b = 2

def enclosed():
    # 함수 바깥의 a와는 전혀 다름!
    a = 10
    c = 3

    def local(c):
        print(a, b, c)  # 10, 2, 500

    local(500)
    print(a, b, c)  # 10, 2, 3

enclosed()

print(a, b)  # 1, 2
```

- global 키워드: 내부 스코프를 외부 전역 범위로 확장하여 지정하기 위해 사용
```py
num = 0  # 전역 변수

def increment():
    global num  # num를 전역 변수로 선언
    num += 1

print(num)  # 0

increment()

print(num)  # 1
```

## 패킹과 언패킹
- 패킹: 하나의 변수에 다중의 값을 할당하면 내부적으로 하나의 튜플 형태로 할당함.
```py
packed_values = 1, 2, 3, 4, 5
print(packed_values)  # (1, 2, 3, 4, 5)

numbers = [1, 2, 3, 4, 5]
a, *b, c = numbers
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

def my_func(*objects):
    print(objects)  # (1, 2, 3, 4, 5)
    print(type(objects))  # <class 'tuple'>


my_func(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# <class 'tuple'>
```
- 언패킹: 튜플이나 리스트 등의 객체의 요소들을 개별 변수에 할당
```py
packed_values = 1, 2, 3, 4, 5

# 언패킹
a, b, c, d, e = packed_values
print(a, b, c, d, e)  # 1 2 3 4 5
```
