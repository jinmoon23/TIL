'''
테케 + 3가지 반례 다 나오는데 단호하게 '틀렸습니다' 뜹니다 ㅎㅎ
살려주세요
'''
import sys
sys.stdin = open('input.txt')

def sol(N,arr,M):
    # 예산이 충분한 경우 처리
    if M > sum(arr):
        return max(arr)
    # 요청에 대해 배정받은 예산을 담을 리스트
    receive_lst = []
    # 요청과 그대로 배정받을지 삭감이 필요할지 판단할 기준 -> 이 값보다 크면 삭감되어 배정받는다.
    standard = M/N
    # 수식의 상수
    cons = 0
    # 상한값을 의미하는 변수
    x = 0

    for elem in arr:
        if elem <= standard:
            cons += elem
        else:
            x += 1

    # 상한값과 추가 배분에 대한 판단을 위한 연산
    dummy_finite = (M-cons) / x
    dummy = dummy_finite - int(dummy_finite)
    finite = (M-cons) // x if (M-cons) / x > 1 else M

    # 상한값에 기반하여 배정받을 예산을 리스트에 저장
    for elem in arr:
        if elem <= finite:
            receive_lst.append(elem)
        else:
            receive_lst.append(finite)

    # 추가적으로 배분이 가능한 예산
    remainder = M - sum(receive_lst)

    # 추가적으로 배분이 불가능하거나 추가 배분 시 상한값을 넘어서는 경우 처리
    if remainder <= 0 or (sum(arr) - M) * dummy > remainder:
        return max(receive_lst)

    # 차이를 확인하고 remainder를 재분배
    for index,elem in enumerate(receive_lst):
        if elem == arr[index]: continue
        diff = arr[index] - elem
        if remainder >= diff:
            remainder -= diff
            elem += diff
            receive_lst[index] = elem
        else:
            elem += diff - remainder
            remainder -= diff - remainder
            receive_lst[index] = elem
        if remainder <= 0:
            return max(receive_lst)

    return max(receive_lst)

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 지방의 수
    arr = list(map(int,input().split())) # 각 지방의 예산 요청 금액
    M = int(input()) # 총 예산의 금액

    print(sol(N,arr,M))