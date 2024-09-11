'''
항상 "ICN" 공항에서 출발
방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성

tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.

만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다. -> 알파벳 순서가 앞선다? 이거 sort 또는 최소힙?
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.
'''

import sys
sys.stdin = open('input.txt')

def find(start):
    # 1. 종료조건 설정
    if len(stack) == N:
        return
    # 2. 재귀호출 전 동작 설정
    # 재귀호출 시 인자로 전달한 arrival 값을 path[0]과 비교
    # 같은 경우 그 path의 1번째 값(arrival)을 출발점으로 재귀 호출
    for i,path in enumerate(paths):
        if path[0] == start:
            # 2번째 테케같이 동일한 출발지가 2개 이상 존재하는 경우 무한루프 방지
            if i in used_lst: continue
            arrival = paths[i][1]
            # 도착지를 스택에 저장
            stack.append(arrival)
            # 2번째 테케같이 동일한 출발지가 2개 이상 존재하는 경우 무한루프 방지
            used_lst.append(i)
            # 3. 재귀호출
            find(arrival)
    # 3번째 테케의 경우 AAA가 도착지가 되는 경우도 모두 스택에 들어가는 문제가 발생함.
    # 그리고 AAA가 시작점이 되는 재귀함수가 호출되면 if path[0] == start 조건을 충족하지 못해 아래의 코드로 내려감.
    else:
        # 아직 스택이 원하는 종료조건만큼 차지 않았기 때문에
        if len(stack) == N:
            return
        # 아래의 코드가 실행되어 잘못된 순서로 저장된 AAA를 제거함
        stack.pop()
        used_lst.pop()


T = int(input())
for _ in range(T):
    N = int(input())
    START = 'ICN'
    paths = [input().split() for _ in range(N)]
    stack = []
    used_lst = []
    # 도착지를 알파벳 순서대로 정렬
    paths.sort(key=lambda a: a[1])
    find(START)
    print([START]+stack)
