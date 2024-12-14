import sys
sys.stdin = open('input (2).txt')

def is_sudoku():
    # 가로 스도쿠 검증
    for i in range(SUDOKU_NUM):
        row_v = [0] * (SUDOKU_NUM + 1)
        for j in range(SUDOKU_NUM):
            row_v[puzzle[i][j]] += 1
            if row_v[puzzle[i][j]] > 1:
                return 0
    # 세로 스도쿠 검증
    for j in range(SUDOKU_NUM):
        col_v = [0] * (SUDOKU_NUM + 1)
        for i in range(SUDOKU_NUM):
            col_v[puzzle[i][j]] += 1
            if col_v[puzzle[j][i]] > 1:
                return 0
    # 3x3 매트릭스 스도쿠 검증
    for i in range(0,SUDOKU_NUM,3):
        for j in range(0,SUDOKU_NUM,3):
            compare_lst = []
            for k in range(i,i+3):
                for p in range(j,j+3):
                    compare_lst.append(puzzle[k][p])
            for elem in compare_lst:
                if compare_lst.count(elem) > 1:
                    return 0
    return 1
T = int(input())
for tc in range(1,T+1):
    SUDOKU_NUM = 9
    puzzle = [list(map(int,input().split())) for _ in range(SUDOKU_NUM)]
    res = is_sudoku()
    print(f'#{tc} {res}')