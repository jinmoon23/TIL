import sys
sys.stdin = open('input.txt')
# 원하는 시기에 리턴하여 원하는 값을 출력하기 위해 함수를 활용
def sol():
    for p1 in t1_p_lst:
        for p2 in t2_p_lst:
            # 순회하며 가장 깊은 공통조상을 리턴한다.
            if p1 == p2:
                return (p1)

T = int(input())
for tc in range(1,T+1):
    N = int(input()) # 노드의 개수
    E = N - 1
    E_infos = [list(map(int, input().split())) for _ in range(N)]
    find = E_infos.pop()

    tree = [[] for _ in range(N+1)]

    # 인덱스를 자식노드로 / 값을 부모노드로 구성
    for info in E_infos:
        p,c = info[0],info[1]
        tree[c].append(p)

    # 공통조상을 찾고 싶은 노드번호
    t1,t2 = find

    # 자기 자신을 조상으로 가지며 / 부모노드가 발견되지 않을 때 까지 모든 부모노드를 담는다.
    t1_p_lst = [t1]
    t2_p_lst = [t2]

    while tree[t1] != []:
        t1_p_lst.append(tree[t1][0])
        t1 = t1_p_lst[-1]
    while tree[t2] != []:
        t2_p_lst.append(tree[t2][0])
        t2 = t2_p_lst[-1]
    print(sol())