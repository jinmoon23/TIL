import sys
sys.stdin = open('input.txt')

def p_cal(r):

    pass
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    max_len = 0
    for i in range(N):
        if max_len < len(matrix[i]):
            max_len = len(matrix[i])
    print(f'#{tc} {p_cal(max_len)}')
