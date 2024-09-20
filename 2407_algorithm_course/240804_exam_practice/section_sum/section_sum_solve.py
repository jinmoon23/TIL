'''
1. 가장 큰 구간의 합과 가장 작은 구간의 합의 차를 리턴
2. 정수의 개수 N, 구간의 길이 M
3. 정렬 후 맨 앞 M 구간의 합을 맨 뒤 M 구간의 합에서 빼주면 될 듯. -> 정렬하면 안된다!
'''

import sys
sys.stdin = open("input.txt", "r")

def find_section_sum(arr):
    sum_list = []
    for i in range(N-M+1):
        sum_value = sum(arr[i:M+i]) # 한 칸씩 이동하며 구간합 구하기
        sum_list.append(sum_value) # 리스트 요소로는 각 구간합의 값들이 들어가 있다.

    min_value = sum_list[0]
    max_value = sum_list[0]

    for i in range(len(sum_list)):
        if min_value > sum_list[i]:
            min_value = sum_list[i]
        elif max_value < sum_list[i]:
            max_value = sum_list[i] # sum_list의 최대값과 최소값을 구하기

    return max_value - min_value

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f'#{test_case} {find_section_sum(arr)}')