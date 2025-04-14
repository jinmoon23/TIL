T = 3 # 3 가정
for test_case in range(1, T + 1):
    N,K = 5,10

    result_count = 0
    A_set_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    subsets = []
    subset_count = 2**N

    for i in range(subset_count):
        subset = []
        for j in range(N):
            if i & (1 << j):
                subset.append(A_set_list[j])
        subsets.append(subset)

    for subset in subsets:
        if len(subset) == N and sum(subset) == K:
            result_count += 1
    print(result_count)