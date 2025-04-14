# 제어문 및 모듈

## module
- 이미 만들어진 증명된 코드를 활용하는 것
- dot 연산자: 왼쪽의 객체에서 오른쪽의 변수나 함수를 찾아라.
```python
math.sqrt
```

## 파이썬 표준 라이브러리
- 모듈이 모여 패키지가 되고 패키지가 모여 라이브러리가 된다.

request 모듈
```py
import requests

url = 'https://random-data-api.com/api/v2/users'
response = requests.get(url).json() # json() 함수를 통해 데이터를 가공함

print(response)
```

## 제어문
- 조건문
  - if / elif / else
  - 동시검사가 아닌 **순차**검사!
```py
dust = 400

if dust>150:
    print("매우 나쁨")
    if dust>300:
        print('위험해요! 나가지 마세요!')
elif dust>80:
    print('나쁨')
elif dust>30:
    print('보통')
else:
    print('좋음')
```

## 반복문
- 임의의 **시퀀스** 항목들을 **순서대로** 반복
```py
numbers = [1,2,3,4,5]
for i in numbers: # i는 임시변수로 numbers 리시트의 각 원소를 받아 코드블럭에서 사용한다. 
    # 코드블럭
- 딕셔너리에 적용된 반복문
```py
my_dict = {
    'x': 10,
    'y': 20,
    'z': 30,
}

for key in my_dict:
    print(key)
    print(my_dict[key])
```
- 중첩된 반복문
  - 여기서 가장 중요한 점은 외부 코드가 1회 실행 후 내부코드가 마무리 된 후 외부코드가 이후에 실시된다는 점. 
```py
outers = ['A', 'B']
inners = ['c', 'd']

for outer in outers:
    for inner in inners:
        print(outer,inner) ## A,c / A,d / B,c / B,d
```
```py
elements = [['A', 'B'], ['c', 'd']]

for element in elements:
    for item in element:
        print(item) ## A B c d 
```
- while문
  - 조건식이 참일동안 실행되는 반복문 = 거짓이 될 때 까지 반복
```py
a = 0
while a<3:
    print(a)
    a+=1

print('끝')

number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')
```
- 반복 제어
  - continue: 다음 **While 반복**으로 건너뛰기하는 구문 / break는 while 반복문을 벗어나서 다음 코드로 건너뛰기함. 
```py
# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```
  - continue 추가 예시
```py
# continue 예시 - "리스트에서 홀수만 출력하기"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)
```
  - pass: 아무 의미 없음! 나중에 다시 돌아오려고 하는 코드.
```py
# pass
for i in range(10):
    pass
```
- break 예시
```py
# break 예시 2 - "리스트에서 첫번째 짝수만 찾은 후 반복 종료하기"
numbers = [1, 3, 6, 5, 7, 9, 11, 11]
found_even = False

for number in numbers:
    if number % 2 == 0:
        print(f'첫 번째 짝수 {number}을/를 찾았습니다.')
        found_even = True
        print(found_even)
        break
if found_even == False:
    print('짝수를 찾지 못함')
```

## list comprehension
- 명료하고 간결하게 리스트를 작성
- [표현식 for 임시변수 in 리스트]
```py
# 사용 전
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)

# 사용 후

squared_numbers2 = [num**2 for num in numbers] # numbers 리스트의 요소를 제곱해서 리스트로 만들어줘!
print(squared_numbers2)
```

## 참고(enumerate)
- 리스트의 인덱스도 뽑아낼 수 있는 함수
- enumerate(iter,start=0), start 인자는 기본값이 0으로 설정되어 있음. 명시하지 않으면 0부터 시작하지만 직접 명시할수도 있다. 
```py
fruits = ['apple', 'banana', 'cherry']

for index,fruit in enumerate(fruits): # start 생략한 경우(기본값)
    print(f'인덱스 {index}: {fruit}')

for index,fruit in enumerate(fruits,start=3): #3부터 시작
    print(f'인덱스 {index}: {fruit}') 
```