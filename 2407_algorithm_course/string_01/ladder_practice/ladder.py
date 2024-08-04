# 1. 입력 받을 준비
# 2. matrix_size가 0으로 꽉찬 비교 행렬 생성
# 3. 입력받은 행렬(이하 arr)의 0행을 순회하며 1(사다리)을 찾는 if문 구성
# 4. 0행에서 사다리를 찾은 경우 사다리를 타고 내려가며 최종적으로 출발점 j값을 반환하는 함수 작성
import sys
sys.stdin = open('input.txt')

def ladder_game(x,y):
    dxy = [[1,0],[0,-1],[0,1]] # [[아래],[왼쪽],[우측]] 순서로 delta 탐색
    visited = [[0] * matrix_size for _ in range(matrix_size)] # 이 코드가 입력받는 위치에 있으면 무한루프에 빠졌음. 이유는??
    visited[x][y] = 1  # 여기까지가 첫번째 행의 마지막 코드, 맨 아래의 if문을 통과한 후 이므로 현재 위치는 1 위임. 그래서 도장찍는다!

    while x != matrix_size-1: # 행렬의 마지막 행까지 확인
        for dx,dy in dxy: # 3가지 방향에서 아래의 조건을 충족하는 방향은 오직 하나 뿐이다.
            nx = x + dx # 순차적으로 dx에 1, 0, 0 이 대입됨
            ny = y + dy # 순차적으로 dy에 0, -1, 1 이 대입됨

            if nx < 0 or ny < 0 or nx >= matrix_size or ny >= matrix_size: continue # 인덱스 체크
            if arr[nx][ny] == 0: continue # 사다리 체크
            if visited[nx][ny] == 1: continue # 이미 지났던 사다리 체크
            # 위 if문을 모두 통과한 이후 도달하는 코드
            visited[x][y] = 1
            x,y = nx,ny # 이 부분이 실질적으로 사다리를 이동하는 코드임.
    if arr[x][y] == 2:
        return True
    return False

test_case = 10
for tc in range(1,test_case+1):
    test_case_num = int(input())
    matrix_size = 100
    arr = [list(map(int,input().split())) for _ in range(matrix_size)]

    result = -1 # 99행에서 2를 찾지 못한 경우를 식별하기 위한 초기화

    for j in range(matrix_size):
        if arr[0][j] == 0: continue
        if ladder_game(0,j):
            result = j
            break
    print(f'#{tc} {result}')



