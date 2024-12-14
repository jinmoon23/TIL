# 최고점과 최저점의 간격을 줄이기
# 목표 -> 최고점 - 최저점 <= 1
# 작업횟수에 제한이 존재 -> 제한만큼 시행 후 최고점 - 최저점을 리턴하는 함수 작성
# 가로의 길이는 항상 100으로 일정
# 높이의 길이는 1이상 100이하
# 작업횟수는 1000회 이하
# 최종적인 종료조건 -> 최고점 - 최저점 <= 1 or 작업횟수 종료
# 문제의 예시
# work_list = [5,8,3,1,5,6,9,9,2,2,4]

# 풀이과정
# 1. 리스트의 max_value와 min_value의 index를 찾는다.
# 2. max_value의 인덱스로 값에 접근해 -1 한 값을 재할당하고 min_value는 동일하게 +1 한 값을 재할당한다.
# 3. 2의 과정을 마무리하고 work_count를 1 감소시킨다.
# 4. 위의 과정을 work_count가 0이되거나 max_value - min_value <= 1이 될때까지 반복한다.

import sys
sys.stdin = open('input.txt')

test_case_num = 10

def solution(tc, work_list, work_count):
    max_value = max(work_list)  # 9 8
    min_value = min(work_list)  # 1 2
    while max_value - min_value > 1 and work_count != 0: # 9-1>1 이고 work_count == 2이므로 아래코드 진행
        max_value_index = work_list.index(max_value)  # 3
        min_value_index = work_list.index(min_value)  # 0
        work_list[max_value_index] -= 1  # [1,2,3,8]이 됨
        max_value -= 1  # 8이 됨
        work_list[min_value_index] += 1  # [2,2,3,8]이 됨
        min_value += 1  # 2가 됨
        work_count -= 1  # 1이 됨 -> work_count는 1이고 max-min==8 > 1 이므로 반복 지속
        # 해결이 필요한 부분 -> max,min value가 변경되지만 index는 변하지 않는 문제
    # while work_count != 0:
    result = max_value - min_value
    return f'#{tc} {result}'


for tc in range(1, test_case_num + 1):
    work_count = int(input())  # 2 가정
    work_list = list(map(int, input().split()))  # [1,2,3,9] 가정
    print(solution(tc, work_list, work_count))

