'''
접근법
1. arr 총합과 M의 금액을 비교 -> M이 더 큰 경우 예산에 여유가 있음 -> arr 중 최대값 리턴
2. M이 더 작은 경우 예산에 여유가 없음 -> 상한값 설정
3. 상한값은 M의 평균과 arr의 요소를 비교 -> 더 작은 값은 그대로 더 큰 값은 삭감할 필요가 있음
4. 상한액 = x, 110 + 120 + (140-(140-x)) + (150-(150-x)) = 485 -> x = 127.5 -> int(x) == 127
'''

import sys
sys.stdin = open('input.txt')
def sol(N,arr,M):
    remainder = M
    while remainder != 0:
        # 1. 예산총액의 평균을 구하고
        avg_M = (remainder // N) if remainder // N >= 1 else 0
        # 2. 상한값 x를 설정
        cnt = 0
        # 3. 1의 평균보다 작은 값은 그대로 사용할 예정이므로 따로 더해서 모아줌
        little = 0
        index_lst = []
        for index,n in enumerate(arr):
            if n <= avg_M:
                little += n
            # cnt의 존재는 상한값이 필요하다는 의미
            else:
                cnt += 1
                index_lst.append(index)
        remainder = M - (N*cnt) if M >= N*cnt else 0
        divider = remainder // cnt
        for index in index_lst:
            arr[index] += divider
    # 상한값 구하기
    # 110 + 120 + (140-(140-x)) + (150-(150-x)) = 485 -> x = 127.5 -> int(x) == 127 를 수식으로 나타낸 결과
    finite = ((M - little) // cnt)
    # M - little <= 라면
    # 예산이 충분한 경우
    if sum(arr) <= M:
        return max(arr)
    # 예산이 충분하지 않은 경우
    else:
        return finite
T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 지방의 수
    arr = list(map(int,input().split())) # 각 지방의 예산 요청 금액
    M = int(input()) # 총 예산의 금액
    print(sol(N,arr,M))