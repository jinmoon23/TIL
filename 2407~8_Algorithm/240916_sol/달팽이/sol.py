'''
정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
방향 전환은 항상 막다른 길에 봉착한 경우에만 해야한다.
'''

import sys
sys.stdin = open('input (2).txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]
    dxy = [[0,1],[1,0],[0,-1],[-1,0]] # 우 / 하 / 좌 / 상
    # 기본값으로 우측 방향을 설정하기 위해 direction 변수에 0 할당
    i,j,direction,num = 0,0,0,1
    # 최초 시작 지점에 값 할당
    board[i][j] += num

    while num != N**2:
        num += 1
        # % 4 하는 이유 -> N값이 커지더라도 동일한 달팽이 만들기 로직을 유지하기 위함
        dx,dy = dxy[direction % 4]
        nx,ny = i + dx, j + dy
        # 방향전환이 필요한 시점
        if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] != 0:
            direction += 1
            dx,dy = dxy[direction % 4]
            nx, ny = i + dx, j + dy
        board[nx][ny] = num
        # 다음 반복에서 시작하는 지점을 설정
        i,j = nx,ny

    print(f'#{tc}')
    for i in range(N):
        print(*board[i])