'''
N x N 배열
스프레이의 노즐이 + 형태로 되어있어, 스프레이는 + 혹은 x 형태로 분사된다.
스프레이를 M의 세기로 분사하면 노즐의 중심이 향한 칸부터 각 방향으로 M칸의 파리를 잡을 수 있다.
+또는 x 중 하나로 분사된다.
'''
import sys
sys.stdin = open("in1.txt", "r")

def kill_fly(mat):
    dxy_plus = [[0,-1],[-1,0],[0,1],[1,0]] # 좌/상/우/하
    dxy_mul = [[-1,-1],[-1,1],[1,1],[1,-1]] # 좌상/우상/우하/좌하

    result_list = []
    # + 형태 분사
    for i in range(N):
        cnt_list = []
        for j in range(N):
            cnt = 0
            cnt += mat[i][j]
            for k in range(1,M):
                for dx,dy in dxy_plus:
                    if i + (dx*k) >= N or j + (dy*k) >= N or i + (dx*k) < 0 or j + (dy*k) < 0: continue
                    nx = i + (dx*k)
                    ny = j + (dy*k)
                    cnt += mat[nx][ny]
            cnt_list.append(cnt)
        result_list.append(max(cnt_list))
    # x 형태 분사
    for i in range(N):
        cnt_list = []
        for j in range(N):
            cnt = 0
            cnt += mat[i][j]
            for k in range(1,M):
                for dx,dy in dxy_mul:
                    if i + (dx*k) >= N or j + (dy*k) >= N or i + (dx*k) < 0 or j + (dy*k) < 0: continue
                    nx = i + (dx*k)
                    ny = j + (dy*k)
                    cnt += mat[nx][ny]
            cnt_list.append(cnt)
        result_list.append(max(cnt_list))

    return max(result_list)

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split()) # 정방행렬 길이 / 세기(몇 칸의 파리를 잡을 수 있는가)
    fly_matrix = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{test_case} {kill_fly(fly_matrix)}')
