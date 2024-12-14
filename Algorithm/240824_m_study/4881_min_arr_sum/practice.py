import sys
sys.stdin = open("4881_input.txt", "r")

def dfs(i,sm):
    global ans
    if ans <= sm:
        return
    if i == N:
        ans = min(ans,sm)
        return
    for j in range(N):
        if v[j] != 0: continue
        v[j] = 1
        dfs(i + 1,sm + arr[i][j])
        v[j] = 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    v = [0] * N
    ans = 10 * N
    dfs(0,0)
    print(f'#{test_case} {ans}')