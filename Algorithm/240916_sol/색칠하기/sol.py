'''
칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)] # 1 = 빨강 / 2 = 파랑 -> 3 = 보라
    MATRIX_SIZE = 10
    board = [[0]* MATRIX_SIZE for _ in range(MATRIX_SIZE)]

    for elem in arr:
        row, col, color = elem[2]-elem[0]+1, elem[3]-elem[1]+1, elem[4]
        for i in range(row):
            for j in range(col):
                board[elem[0]+i][elem[1]+j] += color
    res = 0
    for i in range(MATRIX_SIZE):
        for j in range(MATRIX_SIZE):
            if board[i][j] == 3:
                res += 1

    print(f'#{tc} {res}')