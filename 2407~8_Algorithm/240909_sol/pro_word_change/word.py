'''
아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성
'''

import sys
sys.stdin = open('input.txt')

def solution(begin, target, words):
    if target not in words: return 0


T = int(input())
for tc in range(1,T+1):
    be, ta = map(str,input().split())
    arr = input().split()

    solution(be,ta,arr)