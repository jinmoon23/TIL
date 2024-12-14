total = 0 # 원소와 인접원소의 차의 절대값의 합
t = 2 # 2
di = [0,1,0,-1]
dj = [1,0,-1,0]

for tc in range(1,t+1):
    array_num = 3 # 5
    arr = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ] # 5x5 테이블
    for i in range(array_num):
        for j in range(array_num):
            for k in range(4):
                ni = i + di[k]  # 0번째 오른쪽 / 1번째 밑 / 2번째 왼쪽 / 3번째 위
                nj = j + dj[k]
                if 0 <= ni < array_num and 0 <= nj < array_num:
                    total += abs(arr[i][j] - arr[ni][nj])
    print(f'#{tc} {total}')
