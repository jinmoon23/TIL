
import sys
sys.stdin = open('sample_input.txt')

def find_section_sum(arr):
    sum_list = []
    for i in range(N-M+1):
        sum_value = sum(arr[i:M+i])
        sum_list.append(sum_value)

    min_value = sum_list[0]
    max_value = sum_list[0]

    for i in range(len(sum_list)):
        if min_value > sum_list[i]:
            min_value = sum_list[i]
        elif max_value < sum_list[i]:
            max_value = sum_list[i]

    return max_value - min_value


T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f'#{test_case} {find_section_sum(arr)}')