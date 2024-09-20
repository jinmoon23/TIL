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

# import sys
# sys.stdin = open('input.txt')

test_case_num = 1


def solution(tc,work_list,work_count):
    max_value = max(work_list) # 4
    min_value = min(work_list) # 1
    while work_count != 0 or max_value - min_value  > 1:
        max_value_index = work_list.index(max_value) # 3
        min_value_index = work_list.index(min_value) # 0
        work_list[max_value_index] -= 1 # [1,2,3,3]이 됨
        max_value -= 1 # 3이 됨
        work_list[min_value_index] += 1 # [2,2,3,3]이 됨
        min_value += 1 # 2가 됨
        work_count -= 1 # 3이 됨
        print(work_list)
        # print(max_value)
        # print(min_value)
    result = max_value - min_value
    return f'#{tc} {result}'
    
for tc in range(1,test_case_num+1):
    work_count = 4 # 4 가정
    work_list = [1,2,3,4] # [1,2,3,4] 가정
    print(solution(tc,work_list,work_count))

