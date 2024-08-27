'''
주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램
주어지는 트리는 부모와 자식 노드 번호 사이에 특별한 규칙이 없고, 부모가 없는 노드가 전체의 루트 노드가 된다.
'''

import sys
sys.stdin = open('sample_input.txt')

def count_node(st_n):
    global cnt
    if st_n != 0:
        return
    cnt += 1 # 이 코드의 위치가 핵심. if문 위에 두면 오른쪽 자식 노드를 탐색할 때도 cnt가 올라가는 문제가 발생.
    count_node(tree[st_n][0])
    count_node(tree[st_n][1])

T = int(input())
for test_case in range(1, T + 1):
    E,N = map(int,input().split()) # 간선의 개수 / 루트노드의 번호
    arr = list(map(int,input().split()))

    tree = [[0,0] for _ in range(E+2)] # E는 간선의 개수이고 노드의 총 개수는 간선의 개수에 2를 더해야만 함.
    for i in range(len(arr) // 2):
        p,c = arr[i*2], arr[(i*2)+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
    cnt = 0
    count_node(N)
    print(f'#{test_case} {cnt}')
