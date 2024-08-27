'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13

간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 부모-자식 순서로 표기된다.
전위 순회하여 정점의 번호를 출력하시오.
'''

import sys
sys.stdin = open('input.txt')

def pre_order(node):
    if node == 0:
        return

    print(node, end = ' ') # 이 print 함수의 위치가 어디냐에 따라 전위/중위/후위순회로 나뉜다.
    pre_order(left[node]) # node번 부모가 가진 왼쪽값으로 재귀호출, 12에 도착한 후 재귀호출 시 left[12] == 0 이므로 node = 0이 되어 재귀호출 종료. 즉 pre_order(right[node]) 로 함수가 진행된다. 
    pre_order(right[node]) # node번 부모가 가진 오른쪽값으로 재귀호출

N = int(input())        # 1번부터 N번까지인 정점
E = N-1 # 간선은 정점-1
arr = list(map(int, input().split()))
left = [0]*(N+1)        # 부모를 인덱스로 왼쪽자식번호 저장 ex) left[1] = 2 -> 1번 부모노드의 왼쪽 노드는 2다.
right = [0]*(N+1)       #
par = [0]*(N+1)         # 자식을 인덱스로 부모 저장 ex) par[2] = 1 -> 2번 노드의 부모노드는 1이다.

for i in range(0,len(arr),2): # 간격이 2인 이유는 이진트리이기 때문.
    p,c = arr[i], arr[i+1]
    if left[p] == 0: # left[p] == 0 이라는 말의 의미는 자식노드의 부모 판단이 아직 마무리 되지 않았다는 뜻.
        left[p] = c
    else:
        right[p] = c
    par[c] = p # 순회가 마무리되고 나면 어떤 노드의 부모가 무슨 노드인지가 배열에 저장된다.

c = N
while par[c]!=0:        # 부모가 있으면
    c = par[c]          # 부모를 새로운 자식으로 두고
root = c                # 더이상 부모가 없으면 root
print(root)
pre_order(root)
