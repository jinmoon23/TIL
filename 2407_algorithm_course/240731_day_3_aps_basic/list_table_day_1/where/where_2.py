import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1,test_case+1):
    table,word_len = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(table)]
    result = 0

    new_arr = [[0] * (table + 2)]
    for row in arr:
        new_arr.append([0] + row + [0]) # 양 옆 0
    new_arr.append([0] * (table + 2)) # 위 아래 0

    for i in range(table+word_len):
        for j in range(table+word_len):
            if new_arr[i][j] == 1 and new_arr[i][j-1] == 0 and new_arr[i][j+word_len] == 0:
                result += 1

    for i in range(table+word_len):
        for j in range(table+word_len):
            if i < j:
                new_arr[i][j], new_arr[j][i] = new_arr[j][i], new_arr[i][j]

    for i in range(table+word_len):
        for j in range(table+word_len):
            if new_arr[i][j] == 1 and new_arr[i][j-1] == 0 and new_arr[i][j+word_len] == 0:
                result += 1

    print(f'#{tc} {result}')