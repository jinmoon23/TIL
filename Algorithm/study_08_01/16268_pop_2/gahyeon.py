import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    h, y = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(h)]

    di = [0, 0, 1, 0, -1]  # 델타 탐색 활용
    dj = [0, 1, 0, -1, 0]
    maxi = 0  # 최대 꽃가루 수를 담을 변수 선언 및 정의

    for i in range(h):  # 행만큼 반복
        for j in range(y):  # 열만큼 반복
            total = 0  # 꽃가루의 수 담을 변수 선언 및 정의
            for k in range(5):  # 델타탐색 수만큼 반복
                ni = i + di[k]
                nj = j + dj[k]

                if 0 <= ni < h and 0 <= nj < y:
                    total += lst[ni][nj]  # 5군데에 탐색 돌며 s에 꽃가루 개수 저장

                if maxi < total:  # 최대로 지정간 값보다 한 지점마다 순회한 델타탐색의 합계가 더 많다면
                    maxi = total  # total값을 새로이 최댓값으로 지정

    print(f'#{test_case} {maxi}')