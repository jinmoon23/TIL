'''
N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
죽은 파리의 개수를 구하라!

문제접근
1. fly_matrix에 접근한 후
2. fly_killer_matrix(파리채)를 포개서 해당하는 부분만 추출하여 더한다.
3. 이후 최대값을 리턴
'''

import sys
sys.stdin = open('input.txt')

def fly_killer(matrix):
    kill_count_list = []
    for i in range(fly_matrix_len):
        for j in range(fly_matrix_len):
            kill_count = 0
            for k in range(fly_killer_len):
                for o in range(fly_killer_len):
                    if k+i >= fly_matrix_len or o+j >= fly_matrix_len: continue
                    kill_count += matrix[k+i][o+j]
            kill_count_list.append(kill_count)

    max_value = kill_count_list[0]
    for i in range(len(kill_count_list)):
        if max_value < kill_count_list[i]:
            max_value = kill_count_list[i]

    return max_value




T = int(input())
for test_case in range(1, T + 1):
    fly_matrix_len, fly_killer_len = map(int,input().split())
    fly_matrix = [list(map(int,input().split())) for _ in range(fly_matrix_len)]
    print(f'#{test_case} {fly_killer(fly_matrix)}')