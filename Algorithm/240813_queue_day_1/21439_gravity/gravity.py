'''
방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 가장 큰 낙차를 구하여라
벽에서 떨어져서 쌓인 상자는 없다.
방의 세로 길이는 항상 100이다. 즉, 상자는 최소 0, 최대 100 높이로 쌓을 수 있다

문제접근
1. 가장 큰 낙차이기 위한 조건은 아래와 같다.
    1-1. 초기 상태에서 가장 큰 높이를 가지고
    1-2. 인덱스가 작으면 작을수록(왼쪽벽에 붙어있을수록) 낙차가 크다.
2. ... 이런식으로 접근해서 그림으로 그려봤는데 예외처리가 너무 많이 필요함.

다른 방식의 접근
1. 예시 케이스에서 90도 회전 후의 건물 높이가 5 5 4 4 3 3 2 0 인데 이 높이가 나오는 이유를 분석함
2. 높이가 0인 건물을 제외하고 가장 작은 값부터 새로운 배열에 그 값 만큼 1을 해당 인덱스에 더해주면 완성됨.
    2-1. 예를들어 예시 케이스의 건물 크기는 7 4 2 0 0 6 0 7 0인데
    2-2. 가장 작은 값인 2를
    2-3. 새로운 배열을 만들어 맨 앞 인덱스부터 1 1을 append함
    2-4. 1차 순회에서 새로운 배열은 1 1 0 0 0 0 0 0 을 구성하게 됨. 이 과정 반복하면 5 5 4 4 3 3 2 0 배열구성이 완료됨.
3. 완성된 배열의 가장 작은 값과 높이의 차이를 리턴하면 됨.
'''

import sys
sys.stdin = open("sample_input (2).txt", "r")

def gravity(height_list):
    zero_removed_list = []
    for height in height_list:
        if height != 0:
            zero_removed_list.append(height)

    turned_list = [0] * HEIGHT
    for height in zero_removed_list:
        for i in range(height):
            turned_list[i] += 1

    result_list = []
    for height in turned_list:
        if height != 0:
            result_list.append(height)

    min_value = result_list[0]
    for i in range(len(result_list)):
        if min_value > result_list[i]:
            min_value = result_list[i]

    return structures - min_value


T = int(input())
for test_case in range(1, T + 1):
    HEIGHT = 100
    structures = int(input())
    structures_height_list = list(map(int,input().split()))
    # structures_height_list = [3, 2, 3, 4, 5, 6, 7]
    print(f'#{test_case} {gravity(structures_height_list)}')
