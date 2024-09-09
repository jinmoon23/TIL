'''
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
'''


import sys
from collections import deque
sys.stdin = open('input.txt')

def bfs(start):
    v[start] = 1
    q = deque()
    q.append(start)

    while q:
        start = q.popleft()
        for connect in connections[start]:
            q.append(connect)
        if v[start] == 1: continue
        v[start] = 1
        print(start)


T = int(input())
for _ in range(T):
    N = int(input())
    computers = [list(map(int,input().split())) for _ in range(N)]
    v = [0] * N
    net_lst = []
    for i in range(N):
        for j in range(N):
            if i == j: continue
            if i > j: continue
            if computers[i][j] == 1 and computers[j][i] == 1:
                net_lst.append([i,j])

    connections = [[] for _ in range(N)]
    for net in net_lst:
        s,e = net[0],net[1]
        connections[s].append(e)
        connections[e].append(s)

    bfs(0)
    print(net_lst)
    print(connections)