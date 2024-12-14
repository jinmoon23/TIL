# 지정된 도착점과 대응되는 출발점 리턴
# 사다리는 연속된 1로 표시, 도착점은 2로 표시, 사다리가 아니면 0으로 표시

# 1. 첫 행을 순회하면서 1이 식별되면 아래로 이동, 이동하면서 계속 좌우의 값을 확인
# 2. 좌우 중 1이 발견되면 그 방향으로 이동, 이동하면서 아래의 값을 계속 확인
# 3. 아래에서 1이 발견되면 그 방향으로 이동
# 4. 위 과정을 반복하다가 2를 발견하면 첫 행의 시작점 값을 리턴

# 문제
# 1. 이동을 어떻게 구현할 것인가?

import sys
sys.stdin = open('input.txt')

test_case = 10

def ladder_game(tc,arr):
    di = [0,1,0] # 순서: 오른쪽 / 아래 / 왼쪽
    dj = [1,0,-1] # 순서: 오른쪽 / 아래 / 왼쪽
    for i in range(100):
        for j in range(100):





for tc in range(1,test_case+1):
    test_arr = [list(map(int,input().split())) for _ in range(100)] # 100x100 행렬 생성
    print(ladder_game(tc,test_arr))
