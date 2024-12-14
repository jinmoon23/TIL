
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # 정수의 개수 / 구간의 개수
    arr = list(map(int,input().split()))

    i = 0
    min_v = N * 10000
    max_v = 0
    while i != N-M+1:
        dummy = 0
        for j in range(M):
            dummy += arr[j+i]
        i += 1 # 리스트를 한칸씩 이동하기 위한 재할당
        if min_v > dummy:
            min_v = dummy
        if max_v < dummy:
            max_v = dummy

    print(f'#{tc} {max_v-min_v}')