'''
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프에 대한 정보가 주어질 때, 특정한 두 개의 노드에 경로가 존재하는지 확인하는 프로그램을 만드시오.
두 개의 노드에 대해 경로가 있으면 1, 없으면 0을 출력한다.
노드번호는 1번부터 존재하며, V개의 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
'''
import sys
sys.stdin = open("4871_input.txt", "r")

def dfs():
    stack.append()
T = int(input())
for test_case in range(1, T + 1):
    V,E = map(int,input().split()) # 노드의 개수 / 간선의 개수
    paths = [list(map(int,input().split())) for _ in range(E)]
    check_path = list(map(int,input().split()))
    stack = []
    graph = [[]*E]
