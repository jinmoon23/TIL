'''
항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가한다.
조건 : 부모 노드의 값 < 자식 노드의 값
새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 때까지 부모 노드와 값을 바꾼다.
입력 순서대로 이진 최소힙에 저장
마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램
7, 2, 5, 3, 4, 6이 '차례로' 입력되면!!!!
'''

import sys
sys.stdin = open("sample_input.txt", "r")

def make_heap(node):
    if node > N//2: return
    if node*2+1 <= N:
        c,l,r = arr[node], arr[node*2],arr[node*2+1]
        tree[node], tree[node * 2], tree[node*2+1] = c,l,r
        if c > l:
            tree[node], tree[node * 2] = l,c
            arr[node], arr[node * 2] = arr[node * 2], arr[node]
        elif c > r:
            tree[node], tree[node * 2+1] = r, c
            arr[node], arr[node * 2+1] = arr[node * 2+1], arr[node]
        else:
            tree[node*2] = l
    else:
        l = arr[node*2]
        tree[node*2] = l
    make_heap(node+1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [0] + list(map(int,input().split())) # [0, 7, 2, 5, 3, 4, 6]
    tree = [0] * (N+1)
    tree[1] = arr[1]
    make_heap(1)
    print(tree) # [0, 7, 2, 5, 3, 4, 6]
    p_idx = N // 2
    res = 0
    while p_idx != 1:
        res += tree[p_idx]
        p_idx = p_idx // 2
        if p_idx == 1:
            res += tree[p_idx]

    print(f'#{test_case} {res}')
