arr = [
    [1, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1]
]
table = 8
word_len = 3
result_count = 0

for i in range(table):
    dummy_count = 0
    for j in range(table):
        a_list = arr[i][j:word_len + j]
        if len(a_list) == 3:
            a = sum(arr[i][j:word_len + j])  # [0,0,1] / [0,1,1] / [1,1,1]
            print(a_list)
            if a == word_len:
                dummy_count += 1
    if dummy_count == 1:
        result_count += 1
    else:
        pass

for i in range(table):
    for j in range(table):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for i in range(table):
    dummy_count = 0
    for j in range(table):
        a_list = arr[i][j:word_len + j]
        if len(a_list) == 3:
            a = sum(arr[i][j:word_len + j])  # [0,0,1] / [0,1,1] / [1,1,1]
            print(a_list)
            if a == word_len:
                dummy_count += 1
    if dummy_count == 1:
        result_count += 1
    else:
        pass

print(result_count)