import sys
sys.stdin = open("sample_input.txt", "r")

def enqueue(compare):
    while compare // 2: # 이 표현식이 0이되어 while을 탈출한다는 것의 의미 = 부모노드가 없다. 즉, 비교할 대상이 더이상 존재하지 않는다. -> 루트노드에 도착했다!!
        p = compare // 2 # compare 노드의 부모노드 식별(완전이진트리이기 때문에 가능한 접근법)
        if tree[p] > tree[compare]:
            tree[p], tree[compare] = tree[compare], tree[p]
            compare = p # compare가 4, p가 2인 경우 compare가 2로 재할당되어 p가 1이된다. 즉, 4번 노드와 그 부모노드를 비교하고 재할당을 통해 2번 노드와 그 부모노드를 비교하는 것. 
        else:
            return

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    tree = [0] # 노드를 인덱스로 접근할 것이기 때문에 0을 포함하는 배열로 초기화
    l_node = 0 # 마지막 노드를 식별하여 그 조상 노드들에 접근하는 용도와 enqueue함수의 인자로서 비교할 값에 접근하는 용도의 변수.
    for e in arr:
        tree.append(e) # tree에 일단 넣고
        l_node += 1 # 부모노드의 값과 비교를 진행할 노드의 값에 접근하기 위함
        enqueue(l_node) # 그 노드번호로 함수 호출
    print(tree)

    p_idx = l_node // 2
    res = 0
    while p_idx != 1:
        res += tree[p_idx]
        p_idx = p_idx // 2
        if p_idx == 1:
            res += tree[p_idx]

    print(f'#{test_case} {res}')
