'''
우승을 하게 되면 보너스 상금
주어진 숫자판들 중에 두 개를 선택에서 정해진 횟수만큼 서로의 자리를 위치를 교환할 수 있다.
정해진 횟수만큼 교환이 끝나면 숫자판의 위치에 부여된 가중치에 의해 상금이 계산된다.
반드시 횟수만큼 교환이 이루어져야 하고 동일한 위치의 교환이 중복되어도 된다.
94의 경우 2회 교환하게 되면 원래의 94가 된다.
교환했을 때 받을 수 있는 가장 큰 금액을 리턴

접근법
[3,2,8,8,4]
[3,8,2,8,4]
[8,3,2,8,4] 3가지 케이스를 가정하자

1. if max()의 인덱스가 0보다 크면 그 max() 값을 리스트에서 뽑아내 임의의 []에 저장
2. [3,2,8,4]에 대해 다시 1번 실행 (N이 2라고 가정)
3. 반복이 종료되고 나면 [3,2,4] 와 [8,8] 배열이 각각 완성됨
4. [8,8] 배열에 [3,2,4] 배열을 더하면 완성

만약 [8,3,2,8,4]의 경우
1. if max()의 인덱스가 0보다 크지 않더라도 그 max() 값을 리스트에서 뽑아내 임의의 []에 저장
2. [3,2,8,4]에 대해 1번 반복을 재실행.
3. 반복이 종료되고 나면 [3,2,4] 와 [8,8] 배열이 각각 완성됨
4. [8,8] 배열에 [3,2,4] 배열을 더하면 완성
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    p,c = input().split() # 상금 / 기회

    # p로 받아온 상금 input str을 비교하기 위해 정수형으로 변환하여 리스트에 담는다.
    p_lst = list(map(int,p))
    idx_lst = [] # 원본배열에서의 인덱스

    for j,elem in enumerate(p_lst):
        max_v = max(p_lst)
        if elem == max_v:
            idx_lst.append(j)
    cnt = 0
    compare_lst = []
    while True:
        if cnt >= int(c):
            break
        for idx in idx_lst:
            p_lst[cnt], p_lst[idx] = p_lst[idx],p_lst[cnt]
            cnt += 1
            compare_lst.append(''.join(list(map(str,p_lst))))
    print(compare_lst)