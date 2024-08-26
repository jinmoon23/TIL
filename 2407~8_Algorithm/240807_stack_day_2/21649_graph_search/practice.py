import sys
sys.stdin = open("input.txt", "r")

def dfs(sp):
    global res_lst
    stack = []
    v = [0] * (V + 1)
    v[sp] = 1
    stack.append(sp)
    res_lst.append(sp)
    while True:
        if v[sp] == 0:




test_case = 1
V,E = map(int,input().split())
paths = list(map(int,input().split()))
linked_lst = [[] for _ in range(V+1)]
for i in range(E):
    index, lnk = paths[i*2], paths[(i*2)+1]
    linked_lst[index].append(lnk)
    linked_lst[lnk].append(index)
res_lst = []
sp = 1
dfs(sp)


# print(f'#{test_case} {find_dfs_path(point_arr)}')