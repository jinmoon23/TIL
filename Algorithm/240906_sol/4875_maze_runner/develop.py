'''
출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
0은 통로, 1은 벽, 2는 출발, 3은 도착이다.
'''

import sys
sys.stdin = open('4875_input.txt')

def is_maze_breaker(row,col):
    dxy = [[0,-1],[-1,0],[0,1],[1,0]] # 좌 / 상 / 우 / 하
    stack.append((row, col))
    while stack:
        for dx,dy in dxy:
            nx = row + dx
            ny = col + dy
            # 인덱스 에러 방지
            if nx < 0 or ny < 0 or nx >= N or ny >= N: continue
            # 미로의 벽인지 판단
            if maze[nx][ny] == '1': continue
            # 방문여부 확인
            if v[nx][ny] == 1: continue
            if maze[nx][ny] == '3':
                return 1
            # 위 조건을 모두 충족하지 못한 경우

            # 현 위치 방문기록을 남기고
            v[row][col] = 1
            # 갈 위치 스택에 저장
            stack.append((nx,ny))
        # 4방향에 대한 모든 과정이 완료된 후 이동
        row,col = stack.pop()
    return 0
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    maze = [input() for _ in range(N)] # 0은 통로, 1은 벽, 2는 출발, 3은 도착이다.
    v = [[0]*N for _ in range(N)]
    stack = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                print(f'#{tc} {is_maze_breaker(i,j)}')