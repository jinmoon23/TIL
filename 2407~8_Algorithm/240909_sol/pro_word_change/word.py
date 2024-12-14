'''
아래와 같은 규칙을 이용하여 begin에서 target으로 변환하는 가장 짧은 변환 과정을 찾으려고 합니다.
1. 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
2. words에 있는 단어로만 변환할 수 있습니다.
최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return 하도록 solution 함수를 작성
'''

import sys
sys.stdin = open('input.txt')

def solution(begin):
    global cnt
    # 1. 종료조건 설정
    if begin == tar:
        return
    # 2. 재귀호출 전 동작 설정
    # 문자열의 각 자리 char를 set에 모아서 하나씩 다 변환해서 비교하기
    for i in range(len(begin)):
        d_set = set()
        for word in arr:
            # 같은 char인 경우 early return
            if word[i] == begin[i]: continue
            d_set.add(word[i])
        # 모여진 set값을 활용해 begin 인자 변환
        for d in d_set:
            comp = begin.replace(begin[i],d)
            # 같으면 early return
            if comp == begin: continue
            # 이미 확인했던 char 또는 word early return
            if d in used_lst: continue
            if comp in used_lst: continue

            if comp in arr:
                used_lst.append(d)
                used_lst.append(comp)
                cnt += 1
                #3. 재귀호출
                solution(comp)

T = int(input())
for tc in range(1,T+1):
    be, tar = map(str,input().split())
    arr = input().split()
    cnt = 0
    # 확인했던 값 확인하기 위한 리스트
    used_lst = []
    # 타겟 문자열이 입력 리스트에 존재하지 않으면 재귀호출을 시작할 이유가 없음
    if tar not in arr:
        print(cnt)
    else:
        solution(be)
        print(cnt)
