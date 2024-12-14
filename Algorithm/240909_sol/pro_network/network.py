'''
컴퓨터의 개수 n, 연결에 대한 정보가 담긴 2차원 배열 computers가 매개변수로 주어질 때,
네트워크의 개수를 return 하도록 solution 함수를 작성하시오.
'''


import sys
sys.stdin = open('input.txt')

def dfs(start):
    # 1. visited 배열과 if문에 의한 종료조건 설정
    # 2. 재귀호출 전 동작 설정
    v[start] = 1
    for next_node in connections[start]:
        if v[next_node] == 1: continue
        # 3. 재귀호출
        dfs(next_node)

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
            # 연결되어 있다면 그 인덱스를 저장
            if computers[i][j] == 1 and computers[j][i] == 1:
                net_lst.append([i,j])
    print(net_lst) # [[0, 1]] -> 0번과 1번 컴퓨터는 상호 연결되어 있다.
    # 상호 연결되어 있는 상태를 저장
    connections = [[] for _ in range(N)]
    for net in net_lst:
        s,e = net[0],net[1]
        connections[s].append(e)
        connections[e].append(s)
    print(connections) # [[1], [0], []] -> 0번 컴퓨터는 1번 컴퓨터와 연결되어 있고 1번 컴퓨터는 0번 컴퓨터와 연결되어 있다.
    cnt = 0
    for i,c in enumerate(v):
        if c == 0:
            # 인덱스 값으로 dfs 함수 호출
            dfs(i)
            cnt += 1
    print(cnt)