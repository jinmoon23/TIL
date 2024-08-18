import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive_arr = sorted(list(map(int, input().split())))

    possible = True

    for i in range(N):
        time = arrive_arr[i]
        # time까지 만든 붕어빵 수 = (time // M) * K
        if (time // M) * K < i + 1:
            possible = False
            break

    if possible:
        print(f'#{test_case} Possible')
    else:
        print(f'#{test_case} Impossible')
