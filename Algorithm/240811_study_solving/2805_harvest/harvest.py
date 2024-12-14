'''
N X N크기의 농장
농장은 크기는 항상 홀수
수확은 항상 농장의 크기에 딱 맞는 정사각형 마름모 형태로만 가능
농장의 크기 N와 농작물의 가치가 주어질 때, 규칙에 따라 얻을 수 있는 수익은 얼마인지 구하여라.

문제접근
1. farm의 중심은 항상 (farm_size // 2, farm_size // 2) 임!
    ex) farm_size가 7인 경우 (3,3)이 수확의 중심
    ex) farm_size가 11인 경우 (5,5)이 수확의 중심
2. 수확의 중심을 포함하는 십자가는 항상 수확에 포함된다.

풀이
1. 수확의 중심을 찾는다.
2. 1에서 찾은 중심 행의 모든 값을 더하고 임의설정한 리스트에 그 값을 append한다.
3. 바로 위 행으로 이동하여 특정 조건을 만족하는 행렬의 값을 모두 더하여 1의 리스트에 append한다.

핵심 아이디어
- middle_of_farm을 찾는 것!
'''
import sys
sys.stdin = open("input-6.txt", "r")

def harvest(matrix):
    middle_of_farm = farm_size // 2
    result_list = []
    k = 1 # reverse_farm을 아래로 내리기 위한 변수 -> 더 좋은 방법이 있을 것 같은데..
    for i in range(farm_size):
        if middle_of_farm >= 0:
            result_list.append(sum(matrix[middle_of_farm][i:farm_size-i])) # 한 row씩 올라가면서 수확에 해당하는 행의 일부분을 모두 더함
            middle_of_farm -= 1
        else:
            reverse_farm = (farm_size // 2) +k
            result_list.append(sum(matrix[reverse_farm][i-(farm_size//2):farm_size-i+(farm_size//2)])) # 한 row씩 내려가면서 더함
            reverse_farm += 1
            k += 1

    return sum(result_list)

T = int(input())
for test_case in range(1, T + 1):
    farm_size = int(input())
    farm_matrix = [input() for _ in range(farm_size)]
    farm_int_matrix = [[] for _ in range(farm_size)]

    for i in range(farm_size):
        for j in range(farm_size):
            farm_int_matrix[i].append(int(farm_matrix[i][j]))

    print(f'#{test_case} {harvest(farm_int_matrix)}')
