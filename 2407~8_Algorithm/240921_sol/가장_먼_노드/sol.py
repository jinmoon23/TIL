from collections import deque
def solution(n, edge):
    paths = [[] for _ in range(n + 1)]
    for start, end in edge:
        paths[start].append(end)
        paths[end].append(start)
    v = [0] * (n + 1)

    def bfs(start):
        v[start] = 1
        cnt = 0
        q = deque([(start, cnt)])
        while v != [0] + ([1] * n):
            start, cnt = q.popleft()
            cnt += 1
            for end in paths[start]:
                if v[end] == 1: continue
                v[end] = 1
                q.append((end, cnt))
        res = []
        for elem in q:
            res.append(elem[1])
        max_les = max(res)
        return res.count(max_les)

    res = bfs(1)
    return res


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))