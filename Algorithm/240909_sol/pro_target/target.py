'''
n개의 음이 아닌 정수들
순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다.
타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    target = int(input())
    numbers = list(map(int,input().split()))