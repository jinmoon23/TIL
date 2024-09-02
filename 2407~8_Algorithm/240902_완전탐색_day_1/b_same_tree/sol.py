'''
루트가 있는 트리가 주어지고, 두 노드가 주어질 때 그 두 노드의 가장 가까운 공통 조상을 찾는 프로그램을 작성하세요
테스트 케이스의 마지막 줄에 가장 가까운 공통 조상을 구할 두 노드가 주어집니다.

접근법
1.
'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 노드의 개수
    E = N - 1
    E_infos = [list(map(int, input().split())) for _ in range(N)]
    find = E_infos[-1]
    tree = [[0,0] for _ in range(N+1)]
    for info in E_infos:
        tree[info[0]] = info[1]
