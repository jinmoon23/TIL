test_case_num = 1

def solution(tc,work_list,work_count):
    max_value = max(work_list) # 9 / 
    min_value = min(work_list) # 1 / 
    while work_count != 0 and max_value - min_value  > 1:
        max_value_index = work_list.index(max_value) # 3
        min_value_index = work_list.index(min_value) # 0

        work_list[max_value_index] -= 1 # [1,2,3,8]이 됨
        max_value = max(work_list) # 9에 8이 재할당됨
        max_value_index = work_list.index(max_value) # 3
        work_list[min_value_index] += 1 # [2,2,3,8]이 됨
        min_value = min(work_list)
        min_value_index = work_list.index(min_value) # 0

        work_count -= 1 # 3이 됨
    result = max_value - min_value
    return f'#{tc} {result}'
    
for tc in range(1,test_case_num+1):
    work_count = 4 # 4 가정
    work_list = [1,2,3,9] # [1,2,3,9] 가정
    print(solution(tc,work_list,work_count))