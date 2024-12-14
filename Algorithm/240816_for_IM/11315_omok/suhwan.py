def five():
    dy = [1, 0, 1, -1, 0, -1, -1, -1]
    dx = [1, 1, 0, 1, -1, -1, 0, 1]

    for y in range(N):
        for x in range(N):
            for i in range(8):
                cnt = 0
                for j in range(5):
                    ny = y + dy[i] * j
                    nx = x + dx[i] * j
                    if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 'o':
                        cnt += 1
                if cnt == 5:
                    return 'YES'

    return 'NO'


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    result = five()
    print(f'#{tc} {result}')