import sys
sys.stdin = open("input.txt", "r")

def fly_killer(matrix_of_fly):
    sum_list = []
    for i in range(N):
        for j in range(N):
            sum_count = 0
            for k in range(M):
                for o in range(M):
                    if k+i >= N or o+j >= N: continue # index_error 방지
                    sum_count += matrix_of_fly[k+i][o+j]
            sum_list.append(sum_count)
    return max(sum_list)

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split()) # 파리 행렬 / 파리채 크기 행렬
    matrix_of_fly = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{test_case} {fly_killer(matrix_of_fly)}')
