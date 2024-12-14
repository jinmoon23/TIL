'''
길이 이고 1과 0만을 문자로 갖는 단어에서, 어떤 문자를 중심으로 한 가장 긴 데칼코마니의 길이를 알아내는 프로그램을 만드시오.
중심문자를 포함하므로 데칼코마니의 길이는 항상 홀수이다.
데칼코마니가 없는 경우 중심문자만임을 나타내는 1을 출력한다.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1,T+1):
    N = int(input()) # 0과1로 이루어진 단어블럭의 길이
    block = input()
    k = 1
    cnt = 1
    d_lst = []
    for i,char in enumerate(block):
        if i - k < 0 or i + k >= N: continue
        while True:
            if i - k < 0 or i + k >= N:
                if cnt > 1:
                    d_lst.append(cnt)
                    cnt = 1
                    k = 1
                break
            if block[i-k] == block[i+k]:
                cnt += 2
                k += 1
                if i+k >= N:
                    d_lst.append(cnt)
                    cnt = 1
                    k = 1 
                    break
            else: 
                if cnt > 1:
                    d_lst.append(cnt)
                    cnt = 1
                k = 1
                break
    if d_lst:
        print(f'#{test_case} {max(d_lst)}')
    else:
        print(f'#{test_case} {cnt}')
    