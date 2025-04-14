'''
NxM 크기의 격자판에 붙어있는데, 어떤 풍선을 터뜨리면 상하좌우의 풍선이 추가로 터진다.
한 개의 풍선을 선택해 터뜨렸을 때 날릴 수 있는 꽃가루 수 중 최대값을 출력하는 프로그램
'''
import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    dxy = [[0,-1],[-1,0],[0,1],[1,0]] # 좌 / 상 / 우 / 하

    res = 0
    for i in range(N):
        for j in range(M):
            dummy = 0
            dummy += matrix[i][j]
            for dx,dy in dxy:
                nx, ny = i + dx, j + dy
                if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                dummy += matrix[nx][ny]
            if res < dummy:
                res = dummy
    print(f'#{tc} {res}')