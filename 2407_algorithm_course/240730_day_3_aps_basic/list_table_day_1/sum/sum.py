# 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램
# 각 행의 합(100개), 각 열의 합(100개), 대각선의 합(2개)를 전부 하나의 배열에 넣고 최대값 리턴하기

import sys
sys.stdin = open('input.txt')

test_case = 10

for tc in range(1,test_case+1):
    test_case_count = int(input())
    test_list = [list(map(int,input().split())) for _ in range(100)]

    result_list = [] # 202개의 연산결과가 저장될 리스트

    for i in range(100): # 100개의 행 각각의 합을 result_list에 원소로 전달
        result_list.append(sum(test_list[i]))

    for i in range(100):
        dummy_list = []
        for j in range(100):
            dummy_list.append(test_list[j][i]) # 행을 순회하면서 고정된 열의 값에 접근해야하기 때문에 
        result_list.append(sum(dummy_list)) # 이중for문의 변수인 j를 행 순회 변수로 사용하고 이중for문의 상수인 i를 값 접근자로 사용한다.  

    dummy_list = []
    for i in range(100):
        for j in range(100):
            if i == j:
                dummy_list.append(test_list[i][j])
    result_list.append(sum(dummy_list))
    dummy_list.clear()

    for i in range(100):
        for j in range(100):
            if 99-i == j:
                dummy_list.append(test_list[i][j])
    
    result_list.append(sum(dummy_list))

    print(f'#{tc} {max(result_list)}')