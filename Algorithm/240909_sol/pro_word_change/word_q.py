import sys
from collections import deque
sys.stdin = open('input.txt')

def solution(begin):
    global cnt
    # 1 종료조건 설정
    if begin == tar:
        return
    # 문자열의 각 자리 char를 set에 모아서 하나씩 다 변환해서 비교하기
    for i in range(len(begin)):
        d_set = set()
        for word in arr:
            # 같은 char인 경우 early return
            if word[i] == begin[i]: continue
            d_set.add(word[i])
        # 모여진 set값을 활용해 begin 인자 변환
        for d in d_set:
            # 문자열 클래스의 replace 메서드를 사용해 변환이 필요한 부분에 접근 및 변환
            comp = begin.replace(begin[i],d)
            # 변환값이 기본 값과 같으면 비교의 의미가 없으므로 early return
            if comp == begin: continue
            # 이미 확인했던 word early return
            if comp in used_lst: continue
            if comp in arr:
                # 1 종료조건 설정 / 타겟을 찾은 경우 재귀함수 종료
                if comp == tar:
                    return
                q.append(comp)
                used_lst.append(comp)

    # 3. begin 단어에 대한 모든 검사를 완료하고 큐에 담은 후 재귀호출
    solution(q.popleft())
    # 4. 재귀호출 종료 후 동작설정
    cnt += 1
T = int(input())
for tc in range(1,T+1):
    be, tar = map(str,input().split())
    arr = input().split()
    print(arr)
    cnt = 0
    # 확인했던 값 확인하기 위한 리스트
    used_lst = []
    q = deque()
    # 타겟 문자열이 입력 리스트에 존재하지 않으면 재귀호출을 시작할 이유가 없음
    if tar not in arr:
        print(cnt)
    else:
        solution(be)
        print(cnt)
