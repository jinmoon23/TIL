'''
접근법
1. 동일한 숫자가 적힌 카드가 몇 장인지
2. 1의 카드가 가장 많은 숫자가 적힌 카드를 리턴
3. 만약 1의 카드 수가 모두 같다면 그 중 가장 큰 수가 적힌 카드를 리턴
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input()))

