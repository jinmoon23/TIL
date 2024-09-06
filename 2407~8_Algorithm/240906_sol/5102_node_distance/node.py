'''
V개의 노드 개수와 방향성이 없는 E개의 간선 정보
주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램
노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
'''

import sys
sys.stdin = open('sample_input (2).txt')

def recur(start):
    if start == e:
        return
    v[start] = 1
    recur(connections[start])

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split()) #  5<=V=50, 4<=E<=1000
    E_infos = [list(map(int,input().split())) for _ in range(E+1)] # [[1, 4], [1, 3], [2, 3], [2, 5], [4, 6]]
    find = E_infos.pop() # [1, 6]
    v = [0] * (V+1)

    # 인덱스를 기점 노드로 / 값을 연결 노드로 가지는 리스트 구현
    connections = [[] for _ in range(V+1)]
    print(connections)
    for info in E_infos:
        idx, c= info[0],info[1]
        connections[idx].append(c)
        connections[c].append(idx)
    print(connections) # [[], [4, 3], [3, 5], [1, 2], [1, 6], [2], [4]]

    s,e = find
    print(connections[s])
    recur(s)

