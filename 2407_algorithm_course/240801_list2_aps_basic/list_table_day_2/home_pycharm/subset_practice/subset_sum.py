import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int,input().split()))
    subset_count = 2**len(arr)
    subsets = []
    result = 0

    for i in range(subset_count):
        subset = []
        for j in range(len(arr)):
            if i & (1 << j):
                subset.append(arr[j])
        subsets.append(subset)

    for subset in subsets:
        if subset != [] and sum(subset) == 0 : # 문제의 핵심.  subset에는 항상 공집합이 포함되어 있기 때문에 이에 따른 예외처리가 필요함.
            result = 1
    print(f'#{test_case} {result}')