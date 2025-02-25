# 개선사항

1. `zfill()`메서드를 활용해 while문을 제거할 수 있다.
```py
b_elem1 = bin(elem1)[2:].zfill(n)
# while len(b_elem1) < n:
    # b_elem1 = '0' + b_elem1
```

2. `zip()`고차함수를 활용해 2개의 for문을 하나로 합칠 수 있다. 
```
여러 개의 iterable 객체(예: 리스트, 튜플, 문자열 등)를 동시에 순회하며 각 iterable의 동일 인덱스에 위치한 요소들을 하나의 튜플로 묶어 반환
```
또한 enumerate와 zip을 함께 사용할수도 있음.

```py
def solution(n, arr1, arr2):
    t_map = [[0] * n for _ in range(n)]
    
    row = 0
    for elem1 in arr1:
        b_elem1 = bin(elem1)[2:]
        while len(b_elem1) < n:
            b_elem1 = '0' + b_elem1
        # 다루기 쉬운 이진수로 변환
        for i, char in enumerate(b_elem1):
            t_map[row][i] += int(char)
        row += 1
    
    row = 0
    for elem2 in arr2:
        b_elem2 = bin(elem2)[2:]
        while len(b_elem2) < n:
            b_elem2 = '0' + b_elem2
        for i, char in enumerate(b_elem2):
            t_map[row][i] += int(char)
        row += 1

# 위 코드를 아래의 코드로 리팩토링

def solution(n, arr1, arr2):
    t_map = [[0] * n for _ in range(n)]
    
    row = 0
    for elem1, elem2 in zip(arr1, arr2):
        b_elem1 = bin(elem1)[2:].zfill(n)
        b_elem2 = bin(elem2)[2:].zfill(n)
        for i, (char1, char2) in enumerate(zip(b_elem1, b_elem2)):
            t_map[row][i] += int(char1)
            t_map[row][i] += int(char2)
        row += 1
```