'''
정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
'''

import sys
sys.stdin = open('input (2).txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    board = [[1]*N for _ in range(N)]
