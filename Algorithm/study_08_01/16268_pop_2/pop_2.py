import sys
sys.stdin = open("input.txt", "r")

def find_max_flower_powder(matrix):
    dxy = [[-1,0],[0,1],[1,0],[0,-1]] # 위 / 우측 / 아래 / 좌측
    # dx = [-1,0,1,0]
    # dy = [0,1,0,-1]
    final_compare_list = []
    for i in range(N):
        compare_list = []
        for j in range(M):
            dummy_list = []
            dummy_list.append(matrix[i][j])
            for dx,dy in dxy:
                nx = i + dx
                ny = j + dy
                if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                dummy_list.append(matrix[nx][ny])
            compare_list.append(sum(dummy_list))
        final_compare_list.append(max(compare_list))
    return max(final_compare_list)

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{test_case} {find_max_flower_powder(matrix)}')