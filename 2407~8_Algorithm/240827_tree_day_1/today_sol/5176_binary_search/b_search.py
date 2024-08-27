'''
1부터 N까지의 자연수를 이진 탐색 트리에 저장
저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 '루트에 저장된 값'과, 'N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값'을 출력하는 프로그램

문제접근
1. 1~N까지의 값을 완전이진트리에 저장
2. 트리를 중위순회하며 규칙을 만족할때까지 값을 변경

하.. 완전히 잘못 이해했다.
- 중위순회의 순서대로 노드에 값을 넣어주면 됨

'''

import sys
sys.stdin = open('sample_input.txt')

def make_tree(n):
    global cnt

    if n < N+1: # N이 13인 경우 13번 노드까지는 완전 이진트리를 만들어야 하니 채워넣어야 하기 때문!
        make_tree(n*2)
        # 중위순회이기 때문에 이곳에 코드구성
        cnt += 1
        tree[n] = cnt
        make_tree((n*2)+1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N+1)
    cnt = 0
    make_tree(1)
    print(tree)
    print(f'#{test_case} {tree[1]} {tree[N//2]}')