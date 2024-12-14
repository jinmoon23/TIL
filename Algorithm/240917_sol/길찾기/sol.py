'''
A도시에서 출발하여 B도시로 가는 길이 존재하는지 조사하려고 한다.
최대 2개의 갈림길이 존재하고, 모든 길은 일방 통행으로 되돌아오는 것이 불가능하다. -> 한 개의 정점에서 선택할 수 있는 길의 개수도 2개를 넘어가지 않는다.
A와 B는 숫자 0과 99으로 고정된다.
'''
import sys
sys.stdin = open('input (2).txt')

def dfs(start):
    stack = [start]
    while stack:
        for end in paths[start]:
            stack.append(end)
        start = stack.pop()
        if start == 99:
            return 1
    return 0

T = 10
for _ in range(1,T+1):
    tc, V = map(int,input().split())
    arr = list(map(int,input().split()))
    MAX_V = 100
    paths = [[] for _ in range(MAX_V)]

    for i in range(V):
        paths[arr[i*2]].append(arr[i*2+1])
    res = dfs(0)
    print(f'#{tc} {res}')