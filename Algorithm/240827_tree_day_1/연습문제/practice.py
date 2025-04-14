import sys
sys.stdin = open('input.txt')

def search_node(node):
    if node != 0:
        print(node, end=' ')
        search_node(tree[node][0]) # 왼쪽 자식 탐색
        search_node(tree[node][1]) # 오른쪽 자식 탐색

V = int(input()) # 전체 노드의 수
arr = list(map(int,input().split())) # 간선 arr
# tree 리스트의 index == 부모 노드의 번호
tree = [[0,0] for _ in range(V+1)] # +1 하는 이유는 0번 값을 사용하지 않기 위함

for i in range(len(arr) // 2): # //2 를 하지 않으면 밑의 arr[i*2],arr[i*2+1]에서 인덱스에러가 발생함.
    p,c = arr[i*2], arr[i*2+1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
print(tree)

search_node(1)

# par = [0] * (V+1)
# left = [0] * (V+1)
# right = [0] * (V+1)