'''
V개의 노드 개수와 방향성이 없는 E개의 간선 정보
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램
노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
'''

import sys
from collections import deque
sys.stdin = open('sample_input (2).txt')


def bfs(start,end):
    # 1. 시작점과 거리 큐에 삽입
    q.append((start,0))
    while q:
        start,distance = q.popleft()
        # 2. 방문체크
        if v[start] == 1: continue
        # 3. 방문도장찍기
        v[start] = 1
        # 4. 인접노드 큐에 담기
        for connect in connections[start]: # [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]
            # 인접 노드를 층별로 확인하기 때문에 distance +1 을 여기 배치한다.
            q.append((connect,distance+1))
        # 5. 종료조건 설정
        if start == end:
            return distance
    return 0


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split()) #  5<=V=50, 4<=E<=1000
    E_infos = [list(map(int,input().split())) for _ in range(E)] # [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    s,e = map(int,input().split())

    v = [0] * (V+1)
    q = deque()
    # 인덱스를 기점 노드로 / 값을 연결 노드로 가지는 리스트 구현
    connections = [[] for _ in range(V+1)]
    for info in E_infos:
        idx, c= info[0],info[1]
        connections[idx].append(c)
        connections[c].append(idx)
    print(connections) # [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]

    print(bfs(s,e))
