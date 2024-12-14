'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''

import sys
sys.stdin = open('input.txt')

def search_tree(st_n):
    if st_n == 0:
        return
    print(st_n,end=' ') # 전위 순회
    search_tree(tree[st_n][0])
    # print(st_n, end=' ') # 중위 순회
    search_tree(tree[st_n][1])
    # print(st_n, end=' ') 후위 순회
V = int(input())
arr = list(map(int,input().split()))

tree = [[0,0] for _ in range(V+1)]
print(tree)
for i in range(len(arr) // 2):
    p,c = arr[i*2],arr[(i*2)+1] # tree 리스트의 인덱스는 부모노드의 번호, 내부의 값은 인덱스가 0이면 왼쪽 자식 노드의 번호, 1이면 오른쪽 자식 노드의 번호를 의미한다.
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
print(tree) # [[0, 0], [2, 3], [4, 0], [5, 6], [7, 0], [8, 9], [10, 11], [12, 0], [0, 0], [0, 0], [0, 0], [13, 0], [0, 0], [0, 0]]
search_tree(1)
