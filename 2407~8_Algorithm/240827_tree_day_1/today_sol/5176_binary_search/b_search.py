'''
1부터 N까지의 자연수를 이진 탐색 트리에 저장
저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 '루트에 저장된 값'과, 'N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값'을 출력하는 프로그램

문제접근
1. 1~N까지의 값을 완전이진트리에 저장
2. 트리를 중위순회하며 규칙을 만족할때까지 값을 변경
'''

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nums = list(range(1,N+1))
    tree = [[0,0] for _ in range(N+1)]
    p_cnt = N // 2
    for i in range(1,p_cnt+1):
        tree[i][0], tree[i][1] = nums[i], nums[i+1]


