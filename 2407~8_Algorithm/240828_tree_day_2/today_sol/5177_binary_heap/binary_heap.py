'''
항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
조건 : 부모 노드의 값 < 자식 노드의 값
새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.
입력 순서대로 이진 최소힙에 저장
마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램
'''

import sys
sys.stdin = open("sample_input.txt", "r")

def heap(node):
    if node >= N // 2:
        if node * 2> N: return
        if tree[node] > tree[node * 2]:
            tree[node], tree[node * 2] = tree[node * 2], tree[node]
        if node * 2 + 1 > N: return
        if tree[node] > tree[(node * 2) + 1]:
            tree[node], tree[node * 2 + 1] = tree[node * 2 + 1], tree[node]
        return
    if tree[node] > tree[node * 2]:
        tree[node], tree[node * 2] = tree[node * 2], tree[node]
    if tree[node] > tree[(node * 2) + 1]:
        tree[node], tree[node * 2 + 1] = tree[node * 2 + 1], tree[node]
    heap(node * 2)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tree = list(map(int,input().split()))
    tree.insert(0,0)
    heap(1)
    print(tree)
    p_idx = N // 2
    res = 0
    while p_idx != 1:
        res += tree[p_idx]
        p_idx = p_idx // 2
        if p_idx == 1:
            res += tree[p_idx]

    print(f'#{test_case} {res}')
