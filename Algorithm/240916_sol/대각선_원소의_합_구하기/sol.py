import sys
sys.stdin = open('input (2).txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    res = 0

    for i in range(N):
        for j in range(N):
            if i == j:
                v[i][j] = 1
                res += matrix[i][j]

    for i in range(N):
        for j in range(N-1,-1,-1):
            if v[i][j] == 1: continue
            if i+j == N-1:
                v[i][j] = 1
                res += matrix[i][j]
                
    print(f'#{tc} {res}')

