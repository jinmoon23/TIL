'''
길이 N이고 1과 0만을 원소로 갖는 배열에서, 어떤 원소를 중심으로 한 가장 긴 대칭 구간의 길이를 알아내는 프로그램을 만드시오.
중심원소를 포함하므로 대칭 구간의 길이는 항상 홀수이다.
'''

import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    block = input()
    k = 1 # 만약 대칭되는 경우를 찾는 경우 추가적인 대칭을 파악하기 위한 변수
    cnt = 1
    d_lst = []

    for i,char in enumerate(block):
        if i-k<0 or i+k>=N: continue # 인덱스 범위를 벗어나서 탐색하는 경우 방지하기 위한 early return
        while i-k >= 0 and i+k < N and block[i-k] == block[i+k]:
            # 인덱스 범위를 벗어나지 않고 대칭되는 경우 카운트
            cnt += 2
            k += 1
        d_lst.append(cnt)
        cnt = 1
        k = 1
    print(f'#{tc} {max(d_lst)}')


