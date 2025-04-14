'''
집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
해당하는 부분집합이 없는 경우 0을 출력한다.
'''

import sys
sys.stdin = open('input.txt')

def subset_sum(A):
    subset_count = 2**len(A)
    subsets = []
    result = 0
    for i in range(subset_count):
        subset = []
        for j in range(len(A)):
            if i & (1 << j):
                subset.append(A[j])
        subsets.append(subset)
    for element_subset in subsets:
        if len(element_subset) == N and sum(element_subset) == K:
            result += 1
    return result

T = int(input()) # 3 가정
for test_case in range(1, T + 1):
    N,K = map(int,input().split())
    A = [1,2,3,4,5,6,7,8,9,10,11,12]
    print(f'#{test_case} {subset_sum(A)}')