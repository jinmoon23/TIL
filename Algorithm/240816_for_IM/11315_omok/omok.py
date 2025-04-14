'''
N X N 크기의 판
가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램
판의 각 칸에는 돌이 있거나 없을 수 있다.
각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.
돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력
'''

import sys
sys.stdin = open("sample_input (2).txt", "r")
def omok(matrix):
    # 행 검사
    for line in matrix:
        row_cnt = 0
        k = 0
        while k < row:
            if line[k] == 'o':
                row_cnt += 1
            if k+1 < row and line[k+1] != 'o':
                row_cnt = 0
            if row_cnt == 5:
                return 'YES'
            else:
                k += 1
    # 좌 -> 우 대각선
    diagonal_list = []
    if row <= 5:
        for i in range(row):
            for j in range(row):
                if i == j:
                    diagonal_list.append(matrix[i][j])
    else: # 행렬의 길이가 5보다 크면 대각선의 수가 dist만큼 늘어나기 때문에 고려해야 한다.
        dist = row - 5
        for i in range(row):
            for j in range(row):
                if i == j:
                    diagonal_list.append(matrix[i][j])
        for k in range(1,dist+1):
            for i in range(row):
                for j in range(row):
                    if i+k < row and j == i + k: # 상우측 고려
                        diagonal_list.append(matrix[i][j])
        for k in range(1,dist+1):
            for i in range(row):
                for j in range(row):
                    if j+k < row and i == j + k: # 하좌측 고려
                        diagonal_list.append(matrix[i][j])
    dia_cnt = 0
    for index, elem in enumerate(diagonal_list):
        if elem == 'o':
            dia_cnt += 1
        if index+1 >= len(diagonal_list): continue
        if diagonal_list[index+1] != 'o':
            dia_cnt = 0
    if dia_cnt >= 5:
        return 'YES'
    # 우-> 좌 대각선
    other_side_dia_list = []
    if row <= 5:
        for i in range(row):
            for j in range(row):
                if (row-1)-i == j:
                    other_side_dia_list.append(matrix[i][j])
    else:
        dist = row - 5
        for i in range(row):
            for j in range(row):
                if (row-1)-i == j:
                    other_side_dia_list.append(matrix[i][j])
        for k in range(2,dist+2):
            for i in range(row):
                for j in range(row):
                    if i+j == -k: # 좌상측 고려
                        other_side_dia_list.append(matrix[i][j])
        for k in range(dist):
            for i in range(row):
                for j in range(row):
                    if i+j == k: # 우하측 고려
                        other_side_dia_list.append(matrix[i][j])

    dia_cnt_2 = 0
    for index, elem in enumerate(other_side_dia_list):
        if elem == 'o':
            dia_cnt_2 += 1
        if index + 1 >= len(other_side_dia_list): continue
        if other_side_dia_list[index+1] != 'o':
            dia_cnt_2 = 0
    if dia_cnt_2 >= 5:
        return 'YES'
    # 열
    col_matrix = [''] * row
    for j in range(row):
        for i in range(row):
            col_matrix[j] += matrix[i][j]

    for line in col_matrix:
        column_cnt = 0
        k = 0
        while k < row:
            if line[k] == 'o':
                column_cnt += 1
            if k+1 < row and line[k+1] != 'o':
                column_cnt = 0
            if column_cnt == 5:
                return 'YES'
            k += 1
    return 'NO'

T = int(input())
for test_case in range(1, T + 1):
    row = int(input())
    omok_matrix = [input() for _ in range(row)]
    print(f'#{test_case} {omok(omok_matrix)}')