# 4837, 부분집합의 합
# 집합A / 원소 N개 / 원소의 합 K / 원소의 합이 K인 부분집합의 개수를 리턴하는 함수 / 해당하는 부분집합 없으면 0 리턴
# 예) A = {1,2,3} / N = 3 / K = 6 / return 1
# 이 문제에선 A == {1,2,3,4,5,6,7,8,9,10,11,12}
# 원소 N개를 가지는 부분집합을 만들고 그 부분집합의 합이 K인 경우 카운트를 올리도록 작성해보자

import sys
sys.stdin = open("input.txt", "r")

T = int(input()) # 3 가정
for test_case in range(1, T + 1):
    N,K = map(int,input().split()) # N=3 / K=6 가정

    result_count = 0
    A_set_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    subsets = []
    subset_count = 2**len(A_set_list) # 길이가 L인 집합의 부분집합 개수는 2**L이다!!

    for i in range(subset_count): # 부분집합 생성이 가능한 만큼 순회
        subset = [] # 이해에 중요한 키포인트
        for j in range(len(A_set_list)): # 0~11, 총 12번 순회
            if i & (1 << j):
                subset.append(A_set_list[j])
        subsets.append(subset)

    for subset in subsets:
        if len(subset) == N and sum(subset) == K: # 모든 부분집합 중 길이가 N과 동일하고 합이 K와 동일한 경우 count
            result_count += 1

    print(f'#{test_case} {result_count}')