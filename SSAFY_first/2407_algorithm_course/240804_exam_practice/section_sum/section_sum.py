'''
1. 가장 큰 구간의 합과 가장 작은 구간의 합의 차를 리턴
2. 정수의 개수 N, 구간의 길이 M
3. 정렬 후 맨 앞 M 구간의 합을 맨 뒤 M 구간의 합에서 빼주면 될 듯.
'''

import sys
sys.stdin = open("input.txt", "r")

def find_section_sum(arr):

    for i in range(N-1):
        for j in range(N-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] #  버블소팅

    min_section = arr[:M] # 가장 작은 합을 가지는 구간
    max_section = arr[N-M:] # 가장 큰 합을 가지는 구간
    min_value = 0 # 가장 작은 합
    max_value = 0 # 가장 큰 합

    for element in min_section:
        min_value += element
    for element in max_section:
        max_value += element

    return max_value - min_value


T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f'#{test_case} {find_section_sum(arr)}')