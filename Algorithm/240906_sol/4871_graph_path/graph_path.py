'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
경로가 있으면 1, 없으면 0 리턴
핵심은 방향성 그래프라는 것!
'''

import sys
sys.stdin = open('sample_input (2).txt')

def is_possible(start):
    # v[start] = 1
    stack.append(start)
    while True:
        for dir in directions[start]:
            if v[dir] == 1: continue
            # 방문하지 않은 노드인 경우의 동작
            # 방문표시
            v[dir] = 1
            # 돌아갈 수 있도록 스택에 위치 저장
            stack.append(dir)
            start = dir
            # 탐색과정으로 end를 만날 수 있다면 1을 리턴
            if start == e:
                return 1
            # 깊이 우선 탐색을 위한 break
            break
        # 연결되어 있는 노드가 없는 경우
        else:
            # 스택에 값이 있고 여기 도달했다면 e를 찾지 못한 것이므로 추가적인 탐색이 필요함
            if stack:
                start = stack.pop()
            # e를 찾지 못했고 스택에 값도 없다면 모든 노드를 탐색했음에도 불구하고 경로를 찾지 못한것이므로 무한반복 탈출
            else: break
    return 0

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split()) #  5<=V=50, 4<=E<=1000
    E_infos = [list(map(int,input().split())) for _ in range(E)]
    s,e = map(int,input().split())
    stack = []
    v = [0] * (V+1)

    directions = [[] for _ in range(V+1)]
    # 인덱스를 시작노드로, 값을 도착노드로 가지는 리스트 생성
    for info in E_infos:
        p,c = info[0], info[1]
        directions[p].append(c)
    print(f'#{tc} {is_possible(s)}')
