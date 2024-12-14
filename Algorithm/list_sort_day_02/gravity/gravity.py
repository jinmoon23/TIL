# 낙차가 크기 위해선 높이가 높고 왼쪽에 붙어 있어야 한다는 조건이 존재.
# 1차적으로 가장 큰 수를 찾고 ((가로 길이-1) - 건물높이) 의 값이 가장 큰 값을 리턴
import sys
sys.stdin = open('input.txt')

test_case_num = int(input()) # 테스트 케이스의 수

for i in range(1, test_case_num+1):
    test_case_width = int(input())
    test_case_list = list(map(int,input().split()))
    max_of_list = test_case_list[0] # 정수값

    for num in test_case_list: # 가장 큰 값을 찾는 과정
        if max_of_list < num:
            max_of_list = num
    if test_case_list.count(max_of_list) > 1: # 가장 큰 값이 2개 이상 있는 경우
        pass
    else: # 가장 큰 값이 1개만 있는 경우
        find_index = test_case_list.index(max_of_list) # 가장 왼쪽에 붙어 있고 가장 높은 건물의 인덱스를 찾음

    result = test_case_width - find_index -1
    print(result)

