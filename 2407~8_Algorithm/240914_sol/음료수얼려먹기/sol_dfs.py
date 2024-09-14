'''
구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시
얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성

문제분석
- 행렬에서 0이 상하좌우 한 방향으로 연속된 경우 하나의 아이스크림으로 간주한다.
'''

import sys
sys.stdin = open('input.txt')

def dfs(row,col):
    v[row][col] = 1
    dxy = [[0,-1],[-1,0],[0,1],[1,0]] # 좌 / 상 / 우 / 하
    while stack:
        for dx,dy in dxy:
            nx = row + dx
            ny = col + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if matrix[nx][ny] == 1 or v[nx][ny] == 1: continue
            v[nx][ny] = 1
            stack.append((nx,ny))
        row,col = stack.pop()

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                if v[i][j] == 1: continue
                stack = [(i,j)]
                dfs(i,j)
                cnt += 1
    print(cnt)