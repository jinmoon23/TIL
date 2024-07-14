# 자릿수 더하기

## 문제분석
1. 입력으로 받은 자연수를 자릿수별로 자른 후 리스트에 담는다.
2. 리스트의 모든 값을 더하여 출력한다. 
3. 예를들어 6789가 입력으로 주어진 경우 임의의 리스트에 6,7,8,9를 담고 각 인덱스의 값을 모두 더하여 출력한다.

```python
# N은 사용자의 입력을 저장하는 변수이며 사용자의 입력은 기본적으로 문자열 타입으로 지정된다. 
N = input()
# 빈 리스트를 생성한다.
list = []
# for문에서만 사용할 임의의 변수 x를 설정하여 문자열 N을 순회하며 int로 변환된x 값을 list 리스트에 저장한다. 
for x in N:
    list.append(int(x))
# 이 코드까지 진행된 경우 list 리스트에는 list = [6,7,8,9] 값이 저장된다. 
a = list[0]
b = list[1]
c = list[2]
d = list[3]
solution = a + b + c + d
print(solution)
```
## 코드 시각화
![이미지](./images/스크린샷%202024-07-14%20오후%2012.42.37.png)

## 코드 리팩토링
위의 코드는 input이 항상 4자리 숫자라고 가정하는 경우에만 성공적으로 실행이 가능한 불완전한 코드다. 이를 리팩토링하기 위해 solution 변수를 아래와 같이 수정하면 얼마나 짧든 길든 실행이 가능한 코드가 된다. 
```python
N = input()
list = []
for x in N:
    list.append(int(x))
# a = list[0]
# b = list[1]
# c = list[2]
# d = list[3]
# solution = a + b + c + d
# list의 sum 함수를 사용해 list 변수의 모든 값을 더해준다. 
solution = sum(list)
print(solution)
```