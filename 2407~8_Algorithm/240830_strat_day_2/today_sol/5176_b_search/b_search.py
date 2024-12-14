'''
이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
중위순회의 순서를 값으로 가지는 완전이진트리를 만들자.
'''

import sys
sys.stdin = open('sample_input.txt')

def make_b_tree(node):
    global l_n
    if node > N: # N이 6인 경우 7이상의 노드들을 탐색할 이유가 없기 때문
        return
    make_b_tree(node*2)
    l_n += 1
    tree[node] = l_n
    make_b_tree(node*2+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 노드의 개수
    tree = [0] * (N+1) # [0, 0, 0, 0, 0, 0, 0]
    l_n = 0
    make_b_tree(1)

    print(f'#{tc} {tree[1]} {tree[N//2]}')

