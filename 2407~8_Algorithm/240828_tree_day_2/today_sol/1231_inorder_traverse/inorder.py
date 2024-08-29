'''
주어진 트리를 in-order 형식으로 순회했을때 나오는 단어를 출력
완전이진트리

풀이접근
1. input으로 받아온 값 중 가장 앞의 값을 tree의 부모인덱스로 가지고
2. 숫자가 아닌 값을 해당 노드의 값으로 가지고
3. 이후 연속된 숫자 값이 있으면 각각 왼쪽과 오른쪽 자식노드로 tree에 연결

'''
import sys
sys.stdin = open('input.txt')

def inorder(node):
    global res
    if node == 0:
        return
    inorder(tree[node][0])
    res += tree_v[node]
    inorder(tree[node][1])

T = 10
for tc in range(1,T+1):
    N = int(input())
    infos = [input().split() for _ in range(N)]
    tree_v = []
    tree = [[0,0] for _ in range(N+1)]

    for info in infos:
        while len(info) != 4:
            info.append('0')
        for char in info:
            if not char.isdecimal():
                tree_v.append(char)
                break
            if char.isdecimal():
                if info[2] != '0' or info[3] != '0':
                    tree[int(char)][0] = int(info[2])
                    tree[int(char)][1] = int(info[3])
    print(infos)
    res = ''
    inorder(1)
    print(f'#{tc} {res}')
