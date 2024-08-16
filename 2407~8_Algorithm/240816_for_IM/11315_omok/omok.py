'''
N X N 크기의 판
가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램
판의 각 칸에는 돌이 있거나 없을 수 있다.
각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.
돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력

문제접근
1. delta 접근으로 matrix의 8방향을 모두 검사하고 'o'가 발견되면 해당 방향으로 계속 이동하며 count를 올린다.
2. 모든 접근 후 count가 5보다 작으면 NO를 리턴하고 5이상이면 YES를 리턴한다.
'''

import sys
sys.stdin = open("sample_input (2).txt", "r")

def omok(matrix):
    for line in matrix:
        row_cnt = 0
        k = 0
        while k < row:
            if line[k] == 'o':
                row_cnt += 1
                k += 1
            if row_cnt == 5:
                return 'YES'
            k += 1

    diagonal_list = []
    for i in range(row):
        for j in range(row):
            if i == j:
                diagonal_list.append(matrix[i][j])
    dia_cnt = 0
    for elem in diagonal_list:
        if elem == 'o':
            dia_cnt += 1
    if dia_cnt >= 5:
        return 'YES'

    for i in range(row):
        for j in range(row):
            if i < j:
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    dia_list = []
    for i in range(row):
        for j in range(row):
            if i == j:
                dia_list.append(matrix[i][j])
    dia_cnt_2 = 0
    for elem in dia_list:
        if elem == 'o':
            dia_cnt_2 += 1
    if dia_cnt_2 >= 5:
        return 'YES'

    for line in matrix:
        column_cnt = 0
        k = 0
        while k < row:
            if line[k] == 'o':
                column_cnt += 1
                k += 1
            if column_cnt == 5:
                return 'YES'
            k += 1
    return 'NO'








T = int(input())
for test_case in range(1, T + 1):
    row = int(input())
    omok_matrix = [input() for _ in range(row)]
    print(f'#{test_case} {omok(omok_matrix)}')
    print('안녕')