'''
연구실에 있는 총 N 마리의 폰켓몬 중에서 N/2마리를 가져가도 좋다
폰켓몬은 종류에 따라 번호를 붙여 구분
최대한 다양한 종류의 폰켓몬을 가지길 원함
가장 많은 종류의 폰켓몬을 선택하는 방법
그때의 폰켓몬 종류 번호의 개수를 return
'''

def solution(nums):
    # 선택하는 폰켓몬 수
    choice_num = len(nums)//2
    selected_num = nums[0]
    dummy_lst = [selected_num]
    k = 1
    cnt = 1
    '''
    selected_num을 계속 재할당하면서 인덱스를 이동
    일정한 조건이 충족되면 cnt 리턴
    '''
    while cnt < choice_num:
        if k >= len(nums): break
        if nums[k] != selected_num and nums[k] not in dummy_lst:
            dummy_lst.append(nums[k])
            selected_num = nums[k]
            k += 1
            cnt += 1
        else:
            k += 1
    return cnt

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
print(solution([3,5,7,7,5,4,6,8]))