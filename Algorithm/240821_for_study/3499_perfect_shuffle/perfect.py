'''
카드를 퍼펙트 셔플 한다는 것은,
카드 덱을 정확히 절반으로 나누고
나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미한다.
만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다. -> 앞으로 나눠진 카드리스트에 카드 한 장이 더 들어간다는 의미.

테스트케이스 분석(A B C D E F -> A D B E C F)
1. 반으로 나누고 A B C / D E F
2. A 두고 D 두고 B 두고 E 두고 C 두고 F 두고 마무리

테스트케이스 분석 (A B C D E -> A B C / D E -> A D B E C)
1. 반으로 나누고

문제접근
1. N을 2로 나눴을 때 나누어 떨어지는 경우와 그렇지 않은 경우로 구분
2. 슬라이싱으로 원본 리스트에서 2개의 새로운 리스트 만들고 최종 리스트 만들어두고 활용
'''

import sys
sys.stdin = open('sample_input (1).txt')

def shuffle(cards,st_idx):
    res_lst = []
    l_lst = cards[:st_idx]
    r_lst = cards[st_idx:]
    while len(res_lst) != len(cards):
        if l_lst:
            res_lst.append(l_lst.pop(0))
        if r_lst:
            res_lst.append(r_lst.pop(0))
    return res_lst
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cards = list(input().split())
    sec_starter = 0
    if N % 2 == 0:
        sec_starter = N // 2
    else:
        sec_starter = (N // 2) + 1
    print(f'#{tc}',*shuffle(cards, sec_starter))