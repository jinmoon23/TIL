'''

'''


import sys
sys.stdin = open("input.txt", "r")

def fly_killer(matrix_of_fly,matrix_of_killer):
    dxy = [[0,1],[1,1],[1,0]] # 우측 / 우측아래 / 아래 -> M이 2인 경우
    # dxy = [[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0],[1,1]] # M이 3인 경우

    sum_list = []
    for i in range(N):
        for j in range(N):
            sum_count = 0
            sum_count += matrix_of_fly[i][j]
            for dx,dy in dxy:
                nx = i + dx
                ny = j + dy
                if nx > N-1 or ny > N-1: continue
                sum_count += matrix_of_fly[nx][ny]
            sum_list.append(sum_count)

    return max(sum_list)

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split()) # 파리 행렬 / 파리채 크기 행렬
    matrix_of_fly = [list(map(int,input().split())) for _ in range(N)]
    matrix_of_killer = [[0]*M for _ in range(M)]
    print(f'#{test_case} {fly_killer(matrix_of_fly,matrix_of_killer)}')
