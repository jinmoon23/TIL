'''
푸른 자성체의 경우 N극에 이끌리는 성질을 가지고 있고, 붉은 자성체의 경우 S극에 이끌리는 성질이 있다.
테이블 위에 남아있는 교착 상태의 개수
한 쪽 방향으로 움직이는 자성체의 개수가 많더라도 반대 방향으로 움직이는 자성체가 하나라도 있으면 교착 상태에 빠져 움직이지 않는다.
한 줄에 두 개 이상의 교착 상태가 발생할 수도 있다.
자성체는 테이블 앞뒤 쪽에 있는 N극 또는 S극에만 반응하며 자성체끼리는 전혀 반응하지 않는다.
1은 N극 성질을 가지는 자성체를 2는 S극 성질을 가지는 자성체를 의미하며 테이블의 윗부분에 N극이 아래부분에 S극이 위치한다고 가정한다.

문제접근
1. 1을 발견하면 내려간다.
2. 내려가다가 1을 발견하면 멈추고 그 1로 갈아탄다.
3. 다시 내려가다가 2를 발견하면 count를 1 올리고 다시 내려간다.
4. count를 리턴한다.

위 방식으로 접근하니 너무너무너무너무너무 복잡해서 머리가 안돌아감
1. 각 행을 순차적으로 순회하면서 0이 아닌 값을 가지는 행렬의 값을 임의설정한 리스트에 저장
2. 임의설정한 리스트의 1과2가 붙어있는 경우 result +=1 하도록 구성
'''

import sys
sys.stdin = open("input-6.txt", "r")

def find_deadlock(matrix):
    result = 0
    for j in range(matrix_width): # 행렬의 열을 탐색할 것이기 때문에 임의변수를 j로 설정. 이후의 for문에서는 상수로 사용.
        column_number_list = []
        for i in range(matrix_width):
            if matrix[i][j] != 0: # i가 변수이고 j가 상수, i는 0에서99까지의 값을 가짐
                column_number_list.append(matrix[i][j])
        for k in range(len(column_number_list)-1):
            if column_number_list[k+1] == column_number_list[k]+1: # 1 차이나는 연속된 수 이면 result +=1 동작
                result += 1
    return result

T = 10
for test_case in range(1, T + 1):
    matrix_width = int(input())
    magnetic_matrix = [list(map(int,input().split())) for _ in range(matrix_width)]
    print(f'#{test_case} {find_deadlock(magnetic_matrix)}')