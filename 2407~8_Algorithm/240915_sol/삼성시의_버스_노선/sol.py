'''
버스정류장은 1에서 5,000까지 번호가 붙어 있다.
버스노선은 N개
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.

문제접근
- 버스정류장과 버스노선을 구분해야 한다.
'''

import sys
sys.stdin = open('s_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 버스노선의 개수
    arr = [list(map(int,input().split())) for _ in range(N)] # 버스노선 -> [1,3] 인 경우 1번이 기점, 3번이 종점이라는 의미
    P = int(input()) # 버스정류장의 개수
    BUS_STOP = 5000
    stops = [int(input()) for _ in range(P)]
    v = [0] * (BUS_STOP+1)

    for start, end in arr:
        for i in range(start, end+1):
            v[i] += 1
    print(f'#{tc}', end= ' ')
    for stop in stops:
        print(v[stop], end= ' ')
    print()