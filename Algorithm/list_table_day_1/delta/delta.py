import sys
sys.stdin = open('ex1_input.txt')

t = int(input()) # 2
di = [0,1,0,-1]
dj = [1,0,-1,0]
'''
45 15 10 56 23
96 98 99 40 69
96 84 49 46 34
16 64 81 4 11
10 66 85 55 14
'''
for tc in range(1,t+1):
    total = 0  # 원소와 인접원소의 차의 절대값의 합
    array_num = int(input()) # 5
    arr = [list(map(int,input().split())) for _ in range(array_num)] # 5x5 테이블
    for i in range(array_num):
        for j in range(array_num):
            for k in range(4):
                ni = i + di[k]  # 0번째 오른쪽 / 1번째 밑 / 2번째 왼쪽 / 3번째 위
                nj = j + dj[k]
                if 0 <= ni < array_num and 0 <= nj < array_num:
                    total += abs(arr[ni][nj]- arr[i][j]) # 15-45 / 96 - 45 ...
    print(f'#{tc} {total}')
