'''
DP: Dynamic Programming, 동적 계획
그리디(탐욕) 알고리즘과 같이 최적화 문제를 해결하는 알고리즘

DFS: 깊이우선탐색
1. 막힌 길을 만난 경우 미리 저장된 직전 갈림길로 접근해 순차탐색
2. 이를 위해 스택과 재귀구조의 함수를 사용할 수 있다.
'''

# DFS
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''
import sys
sys.stdin = open("input.txt", "r")

def dfs(s,V):
    visited = [0]*(V+1) # 방문한 정점을 표시할 리스트
    # 스택 생성
    stack = []
    print(s)
    visited[s] = 1 # 시작점 방문 표시
    v = s
    while True:
        for w in adjL[v]:
            if visited[w] == 0:
                stack.append(v)
                v = w # w에 방문
                print(v)
                visited[w] = 1 # w에 방문 표시
                break # v부터 다시 탐색, for의 break
        else: # 남은 인접정점이 없어서 break가 걸리지 않은 경우 -> for else 구문
            if stack:
                v = stack.pop()
            else: # 스택에 남은 요소가 없거나 갈림길이 없는 경우
                break # while의 break


T = 1
for tc in range(1,T+1):
    V,E = map(int,input().split()) # V는 숫자 갯수 / E는 인접(연결) 갯수
    adjL = [[] for _ in range(V+1)]
    arr = list(map(int,input().split()))
    for i in range(E):
        v1,v2 = arr[i*2],arr[i*2+1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    print(adjL)