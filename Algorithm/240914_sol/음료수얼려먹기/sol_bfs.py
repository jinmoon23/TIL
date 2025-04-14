import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(row,col):
    v[row][col] = 1
    dxy = [[0,-1],[-1,0],[0,1],[1,0]] # 좌 / 상 / 우 / 하
    while q:
        # dfs와의 결정적인 차이 -> dfs처럼 탐색 이후에 pop 하게되면 완전탐색하지 못한다.
        # 나머지는 100% 동일
        row, col = q.popleft()
        for dx,dy in dxy:
            nx = row + dx
            ny = col + dy
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if matrix[nx][ny] == 1 or v[nx][ny] == 1: continue
            v[nx][ny] = 1
            q.append((nx,ny))

T = int(input())
for _ in range(T):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    v = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1: continue
            if v[i][j] == 1: continue
            q = deque()
            q.append((i,j))
            bfs(i,j)
            cnt += 1
    print(cnt)