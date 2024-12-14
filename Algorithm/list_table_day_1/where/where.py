import sys
sys.stdin = open('input.txt')

# NxN 크기의 테이블
# 검은색 0, 흰색 1 -> 흰색부분에 word_len이 들어갈 수 있음
# word_len은 딱 맞아야함
# 행 순회할 때:
'''
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
'''
test_case = int(input())
for tc in range(1,test_case+1):
    table,word_len = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(table)]
    result = 0

    for i in range(table):
        dummy_count = 0
        for j in range(table):
            a_list = arr[i][j:word_len + j]
            if len(a_list) == word_len:
                a = sum(arr[i][j:word_len + j])  # [0,0,1] / [0,1,1] / [1,1,1]
                if a == word_len:
                    dummy_count += 1
        if dummy_count == 1:
            result += 1
        elif dummy_count > 1 and sum(arr[i]) > table - word_len:
            result += 1
        else:
            pass

    for i in range(table):
        for j in range(table):
            if i < j:
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    result_2 = 0
    for i in range(table):
        dummy_count = 0
        for j in range(table):
            a_list = arr[i][j:word_len + j]
            if len(a_list) == word_len:
                a = sum(arr[i][j:word_len + j])  # [0,0,1] / [0,1,1] / [1,1,1]
                if a == word_len:
                    dummy_count += 1
        if dummy_count == 1:
            result_2 += 1
        else:
            pass

    print(f'#{tc} {result+result_2}')


