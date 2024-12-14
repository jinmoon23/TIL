'''
구조물은 폭 1m, 길이 2m 이상의 직선 형태로 서로 평행 또는 직각으로만 자리하고 있으며,
1mx1m의 해상도의 사진데이터에 구조물이 있는 자리는 1로 나타난다.
사진의 해상도는 NxM이며, 구조물이 있는 곳은 1, 빈 땅은 0으로 표시된다.
교차하거나 만나는 것처럼 보이는 구조물은 서로 다른 깊이에 묻힌 것이므로 직선인 구조물만 고려하면 된다.
평행한 모든 구조물은 서로 1m이상 떨어져 있고, 구조물의 최소 크기는 1x2m이다.
가장 긴 구조물의 길이를 출력

문제접근
1. 서로 평행 또는 직각으로만 자리하고 있다? 그러나 직선인 구조물만 고려하면 된다?
2. 일단 무시하고 풀어보자

풀이
1. 가로 검사 후 max 담기
2. 세로 검사 후 max 담기
3. 담긴 max 중 max 리턴
'''

import sys
sys.stdin = open("input1.txt", "r")

def find_ancient_remains(mat):
    row_list = []
    # 가로 검사
    for i in range(N):
        for j in range(M):
            cnt = 0
            # 1을 만난 경우 카운팅 시작
            if mat[i][j] == 1:
                cnt += 1
                # 가로로 쭉 뻗어가며 검사 / 가로로 이어가는 것이기 때문에 range에 M 중요
                for k in range(1,M):
                    if j+k < M and mat[i][j+k] == 1:
                        cnt += 1
                        # 가로의 막다른길에 도착한 경우 break
                        if j+k == M-1:
                            row_list.append(cnt)
                            break
                    # 다음 가로 값이 0인 경우 지금까지 쌓인 cnt 값을 리스트에 담고 cnt 초기화 및 break
                    elif j+k < M and mat[i][j+k] != 1:
                        if cnt != 0:
                            row_list.append(cnt)
                        cnt = 0
                        break
            # row에 대한 탐색이 모두 종료된 경우 cnt에 쌓인 값을 리스트에 담기. 이 코드가 없으면 00001 의 경우 맨 마지막 열의 1이 리스트에 담기지 않음.
            if cnt != 0:
                row_list.append(cnt)

    # 세로 검사
    col_list = []
    for j in range(M):
        for i in range(N):
            cnt = 0
            if mat[i][j] == 1:
                cnt += 1
                # 여기서 행 검사이기 때문에 range 설정에서 N을 넣어야 함을 캐치하는게 중요.
                for k in range(1, N):
                    # 여기서도 N
                    if i+k < N and mat[i+k][j] == 1:
                        cnt += 1
                        if i + k == N - 1:
                            col_list.append(cnt)
                            break
                    elif i+k < N and mat[i+k][j] != 1:
                        if cnt != 0:
                            col_list.append(cnt)
                        cnt = 0
                        break
            if cnt != 0:
                col_list.append(cnt)
    row_max = 0
    col_max = 0
    row_max += max(row_list)
    col_max += max(col_list)
    if row_max >= col_max:
        return row_max
    else:
        return col_max

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split()) # 정방행렬 행/열
    anc_matrix = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{test_case} {find_ancient_remains(anc_matrix)}')

