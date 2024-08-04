'''
N개의 정수 중 가장 큰 값과 가장 작은 값의 차이를 출력
'''

import sys
sys.stdin = open("input.txt", "r")

def min_max(arr):
    min_value = arr[0]
    max_value = arr[0]

    for i in range(N):
        if min_value > arr[i]:
            min_value = arr[i]
        elif max_value < arr[i]:
            max_value = arr[i]

    return max_value - min_value

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    print(f'#{test_case} {min_max(arr)}')