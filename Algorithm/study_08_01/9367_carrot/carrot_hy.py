import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 1
    max_c = 1

    for i in range(N - 1):
        if arr[i] < arr[i + 1]:
            count += 1
            if max_c <= count:
                max_c = count
        else:
            count = 1

    print(f'#{test_case} {max_c}')