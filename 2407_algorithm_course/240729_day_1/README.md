# Algorithm Day_1

## sort / min / max 등 파이썬 내장함수를 사용하지 않고 min/max 도출하기

```py
T=int(input()) # 테스트케이스 개수

for i in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    max_elem = arr[0] # 어떤 값이 들어가도 무관
    min_elem = arr[0] # 어떤 값이 들어가도 무관

    for elem in arr:
        if max_elem < elem:
            max_elem = elem # 계속해서 재할당 
        elif min_elem > elem:
            min_elem = elem # 계속해서 재할당

    result = max_elem - min_elem
    print(f'#{i} {result}')
```
핵심은 **반복적 재할당**
## bubble sorting
```py
N = 5
arr = [55,7,78,12,42]

# 각 구간의 끝 인덱스 i
# 각 구간에서 두 개씩 비교할 때 왼쪽 원소의 인덱스 j
# 왼쪽 원소가 더 크면 오른쪽 원소와 교환

for i in range(len(arr)-1,0,-1): 
    for j in range(i): # len(arr)-2까지의 인덱스만 사용한다. 만약 그렇지 않은 경우 [j+1]에 indexerror가 발생
        if arr[j] > arr[j+1]:
            arr[j+1],arr[j] = arr[j],arr[j+1]
print(arr)
```
- i에 4,3,2,1 값이 순차적으로 대입되고 j에는 0,1,2,3 / 0,1,2 / 0,1 / 0 값이 순차적으로 대입되며 반복문이 진행된다. 

view 과제 하는중
```py
test_case = 10

for i in range(1,test_case+1):
    test_number = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for elem in arr:
        if elem:
            a = elem - arr[arr.index(elem)-2], elem - arr[arr.index(elem)-1], elem - arr[arr.index(elem)+1], elem - arr[arr.index(elem)+2]
            if min(a) < 0:
                pass
            else:
                count += min(a)

    print(f'#{i} {count}')
```
해결!
```py
test_case = 10

for i in range(1,test_case+1):
    test_number = int(input())
    arr = list(map(int,input().split()))
    count = 0

    for j in range(len(arr)):
        if arr[j]:
            a = arr[j] - arr[j-2],arr[j] - arr[j-1],arr[j] - arr[j+2],arr[j] - arr[j+1]
            if min(a)<0:
                pass
            else:
                count += min(a)

    print(f'#{i} {count}')
```