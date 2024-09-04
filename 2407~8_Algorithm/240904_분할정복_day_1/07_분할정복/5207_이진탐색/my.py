'''
서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장
그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인
B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수 -> 탐색 몇번 하는지 리턴해라.
테스트 케이스의 별로 A와 B에 속한 정수의 개수 N, M이 주어지고, 두 줄에 걸쳐 N개와 M개의 백만 이하의 양의 정수가 주어진다.
'''

import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    # 1. 종료조건 설정
    if len(arr) <= 1:
        # 평소처럼 여기서 아무것도 리턴하지 않으면 언패킹 오류가 발생함.
        return arr
    # 2. 재귀 호출 전 동작
    pivot = arr[0]
    left, equal, right = [], [], []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            equal.append(arr[i])
        else:
            right.append(arr[i])
    # 3. 재귀 호출
    return [*quick_sort(left), *equal, *quick_sort(right)]

def b_search(arr,target,start,end,middle):
    global cnt
    dummy_cnt = 0
    if cnt == 0 and arr[middle] == target:
        cnt += 1
        return
    # left = arr[:middle]
    # right = arr[middle+1:]
    # 우측 탐색
    if target > arr[middle]:
        start = middle + 1
        b_search(arr,target,start,end,(end + start) // 2)
        dummy_cnt += 1
    # 좌측 탐색
    elif target < arr[middle]:
        end = middle
        b_search(arr, target,start,end,(end + start) // 2)
        dummy_cnt += 1
    if dummy_cnt >= 2:
        cnt += 1

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split())) # [1, 2, 3]
    B = list(map(int,input().split())) # [2, 3, 4]
    sorted_A = quick_sort(A)
    cnt = 0
    for elem in B:
        if elem in A:
            start = 0
            end = len(sorted_A) - 1
            middle = (start + end) // 2
            b_search(sorted_A,elem,start,end,middle)

    print(f'#{tc} {cnt}')