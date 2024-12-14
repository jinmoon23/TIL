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
    rows_list = []
    # 가로 검사
    for i in range(N):
        cnt = 0
        for j in range(M):
            # 1을 만난 경우 카운팅 시작
            if mat[i][j] == 1:
                cnt += 1
                # 인덱스 범위를 벗어나거나 해당 인덱스의 다음열 값이 1이라면 "continue", j를 1 이동 -> cnt를 누적시킬 수 있다.
                if j+1 < M and mat[i][j+1] == 1: continue
            else:
                cnt = 0
            if cnt != 0:
                rows_list.append(cnt)
    # 세로 검사
    cols_list = []
    for j in range(M):
        cnt = 0
        for i in range(N):
            if mat[i][j] == 1:
                cnt += 1
                if i+1 < N and mat[i+1][j] == 1: continue
            else:
                cnt = 0
            if cnt != 0:
                cols_list.append(cnt)
    # 값이 없는 경우 발생하는 런타임 에러를 방지하기 위한 변수 초기화
    row_max = 0
    col_max = 0
    row_max += max(rows_list)
    col_max += max(cols_list)
    if row_max >= col_max:
        return row_max
    else:
        return col_max

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split()) # 정방행렬 행/열
    anc_matrix = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{test_case} {find_ancient_remains(anc_matrix)}')

