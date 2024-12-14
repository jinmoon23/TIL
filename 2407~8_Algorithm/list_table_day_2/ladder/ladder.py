# 지정된 도착점과 대응되는 출발점 리턴
# 사다리는 연속된 1로 표시, 도착점은 2로 표시, 사다리가 아니면 0으로 표시

# 1. 첫 행을 순회하면서 1이 식별되면 아래로 이동, 이동하면서 계속 좌우의 값을 확인
# 2. 좌우 중 1이 발견되면 그 방향으로 이동, 이동하면서 아래의 값을 계속 확인
# 3. 아래에서 1이 발견되면 그 방향으로 이동
# 4. 위 과정을 반복하다가 2를 발견하면 첫 행의 시작점 값을 리턴

import sys
sys.stdin = open('input.txt')

test_case = 10
result = -1  # 2를 만나지 못한 경우 -1을 리턴하도록 함
# di = [1, 0, 0]  # 순서: 아래 / 왼쪽 / 오른쪽
# dj = [0, -1, 1]  # 순서: 아래 / 왼쪽 / 오른쪽

# delta를 표현하여 행렬을 이동하는 새로운 방법
dxy = [[1, 0], [0, -1], [0, 1]]

def ladder_game(tc, arr):
    for j in range(matrix_size):
        if arr[0][j] == 0:
            continue # early return, 행렬의 첫번째 행을 순회할 때 0과 만나는 경우 사다리가 연결되지 않은 것이니 곧바로 코드를 종료하고 재순회하도록 함
        # 여기 도달하면 첫 번째줄에서 1을 만난 경우임
        if search_ladder(0, j):
            # 탐색하며 사다리를 내려가는 로직을 포함하는 함수
            # 2를 만난 경우의 시작점은 j이기 때문에, 최종 결과에 저장한다.
            result = j # 첫번째 행의 출발지 j가 저장됨
            break  # for문을 탈출
    return f'#{tc} {result}'


def search_ladder(row, columm):
    # 방향을 전환하여 이동한 직후 이동 직전도 1이기 때문에 이 부분에 대한 예외처리가 필요함. 0으로 바꿔주는 방법 또는 1로 바꿔주는 방법 등.
    visited = [[0] * matrix_size for _ in range(matrix_size)]
    # test_arr와는 별개로 0으로 matix_size를 채운 행렬을 따로 생성함
    # 이동할때마다 이동한 행렬값에 1을 재할당하여 방문체크를 실시함
    visited[row][columm] = 1  # 방문체크 -> 이미 ladder_game 함수 내부의 if문에서 1인 경우에만 해당 함수를 호출하기 때문에 바로 방문체크를 함.

    while row != matrix_size - 1: # 행렬의 가장 마지막 행에 도착할 때 까지 반복.
        # for i in range(3): # 3방향이기 때문에 3
            # ni는 이동한 후의 값
            # ni = row + di[i]
            # nj = columm + dj[i]

        #새로운 방법
        # ni,nj는 이동 후의 인덱스 값이 저장된다.
        for di, dj in dxy:
            ni = row + di
            nj = columm + dj
            # if nx >= 0 and nx < matrix_size and ny>= 0 and n< matrix_size:
            # 매트릭스 범위 안에 있는 경우에만 밑의 코드를 실행함
            if ni < 0 or ni >= matrix_size or nj < 0 or nj >= matrix_size: continue
                # 이동 후의 인덱스가 matrix_size 내부에 없으면 반복을 종료하고 다음 반복으로 이동하도록 설정.
            if test_arr[ni][nj] == 0: continue # "아래 값"이 0인지 1인지 확인하여 0이면 반복을 종료
                # 사다리가 아닌 경우 반복을 종료하고 다음 반복으로 이동하도록 설정.
            if visited[ni][nj]: continue
                # 이미 방문한 경우 반복을 종료하고 다음 반복으로 이동하도록 설정.
            # 이 지점에 도착한 친구들은 범위도 만족하고 사다리고 방문도 안함.
            visited[row][columm] = 1
                # 현재 좌표를 임의로 생성한 행렬에 방문한 것으로 처리한다.
            row, columm = ni, nj
                # 이 코드가 모든 조건을 충족하여 행렬을 이동한 경우임.
    if test_arr[row][columm] == 2:
        return True

    return False

for tc in range(1, test_case + 1):
    test_case_num = int(input())
    matrix_size = 100
    test_arr = [list(map(int, input().split())) for _ in range(matrix_size)]  # 행렬 생성
    print(ladder_game(tc, test_arr))
