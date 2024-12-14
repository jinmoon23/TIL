'''
이미 타이핑 한 문자를 지우는 것은 불가능하다.
속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 할 수 있다.
A와 B가 주어질 때 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값

풀이
1. B를 A와 비교해서 완전히 동일한 경우가 있는 경우 그 만큼을 임의의 문자열로 변환
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    A,B = input().split()

    l_A = len(A)
    l_B = len(B)
    cnt = 0
    i = 0

    while i <= l_A - l_B:
        if A[i:i + l_B] == B:
            cnt += 1
            i += l_B  # B를 사용했으므로 B의 길이만큼 점프
        else:
            i += 1  # 한 글자씩 이동
    res = l_A - (l_B * cnt) + cnt
    print(f'#{tc} {res}')