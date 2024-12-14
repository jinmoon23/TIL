'''
1은 벽 / 2는 시작점 / 3은 도착점
'''

import sys
from collections import deque
sys.stdin = open('input-6.txt')

def run_maze(row,col):
    dxy = [[0,-1],[-1,0],[0,1],[1,0]] # 좌/상/우/하
    v = [[0]*MAZE_SIZE for _ in range(MAZE_SIZE)]
    # 최초 시작점 큐에 삽입
    q = deque([(row,col)])
    v[row][col] = 1

    while q:
        row, col = q.popleft()
        for dx,dy in dxy:
            nx,ny = row + dx, col + dy
            # 인덱스 에러 방지
            if nx < 0 or ny < 0 or nx >= MAZE_SIZE or ny >= MAZE_SIZE: continue
            # 방문 여부 확인
            if v[nx][ny] == 1: continue
            # 벽인지 아닌지 확인
            if maze[nx][ny] == '1': continue
            # 도착점에 도달 가능하면 리턴하고 함수 마무리
            if maze[nx][ny] == '3':
                return 1
            # 진출이 가능한 경우 큐에 넣고 방문체크
            q.append((nx,ny))
            v[nx][ny] = 1
    # 탐색을 모두 완료했음에도 불구하고 도착점을 발견하지 못한 경우 0을 리턴하고 함수 종료
    return 0


T = 10
for _ in range(1,T+1):
    MAZE_SIZE = 16
    tc = int(input())
    maze = [input() for _ in range(MAZE_SIZE)]
    for i, row in enumerate(maze):
        for j, number in enumerate(row):
            if int(number) == 2:
                res = run_maze(i,j)
                print(f'#{tc} {res}')
                break