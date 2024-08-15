# 수확한 순서대로 당근의 크기를 기록
# 연속으로 당근의 크기가 커진경우 그 당근의 개수를 리턴
# 연속된다는 것의 정확한 정의가 필요할 듯
# [4,5,1,2,3] 에서 4,5는 연속되지 않은 것이고 1,2,3은 연속된 것이다. 즉 이 경우 리턴은 3이 되어야 함.
# [5,4,3,2,1]은 연속된 경우가 없으므로 1을 리턴
# [1,3,5,7,9]는? 연속해서 당근의 크기가 커진 것임. 이 경우 리턴값은 5가 됨.
# [1,2,3,4,5]
# [1,3,5,7,9,3,2,3,1,2,5]
# 연속으로 커지는 당근 개수의 최대값을 출력

import sys
sys.stdin = open("input.txt", "r")

def counting_upsize_carrot(carrot_size_list):
    count = 1
    result_count_list = []

    for i in range(N-1):
        if carrot_size_list[i] < carrot_size_list[i+1]:
            count += 1
            if count >= 2:
                result_count_list.append(count)
        else:
            count = 1
            if i == N-2:
                result_count_list.append(count)
    return max(result_count_list)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    carrot_size_list = list(map(int,input().split()))
    print(f'#{test_case} {counting_upsize_carrot(carrot_size_list)}')