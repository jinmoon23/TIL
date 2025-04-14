'''
N X N 크기의 판
가로, 세로, 대각선 중 하나의 방향으로 다섯 개 이상 연속한 부분이 있는지 없는지 판정하는 프로그램
판의 각 칸에는 돌이 있거나 없을 수 있다.
각 문자는 ‘o’또는 ‘.’으로, ‘o’는 돌이 있는 칸을 의미하고, ‘.’는 돌이 없는 칸을 의미한다.
돌이 다섯 개 이상 연속한 부분이 있으면 “YES”를, 아니면 “NO”를 출력
'''
import sys
sys.stdin = open("sample_input (2).txt", "r")
def omok(mat):
    # 행 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            if mat[i][j] == 'o':
                cnt += 1
                if cnt == OMOK_CHECK_NUM:
                    return 'YES'
            else:
                cnt = 0
    # 열 검사
    for j in range(N):
        cnt = 0
        for i in range(N):
            if mat[i][j] == 'o':
                cnt += 1
                if cnt == OMOK_CHECK_NUM:
                    return 'YES'
            else:
                cnt = 0
    # 좌상 -> 우하 대각선 검사
    for i in range(N):
        for j in range(N):
            # 우하 대각선 확인 시 인덱스 범위를 넘어가면 인덱스 에러가 발생하는 것 방지.
            # 예를들어 5x5 행렬에서 (0,1)에서 출발하면 5개를 검색하기도 전에 인덱스 에러가 발생함.
            if i+4 >= N or j+4 >= N: continue
            found = True
            # 대각선 고려가 의미가 있는 지점에서 o가 연속적으로 5개 존재하는지 확인. 하나라도 불가능할 경우 break 후 NO 리턴
            for k in range(OMOK_CHECK_NUM):
                if mat[i+k][j+k] != 'o':
                    found = False
                    break
            if found:
                return 'YES'

    # 우상 -> 좌하 대각선 검사
    for i in range(N):
        for j in range(N):
            # 좌하 방향 대각선에서는 j가 줄어들기 때문에(열이 좌측으로 이동) j-4를 확인
            if i+4 >= N or j-4 < 0: continue
            found = True
            for k in range(OMOK_CHECK_NUM):
                if mat[i+k][j-k] != 'o':
                    found = False
                    break
            if found:
                return 'YES'
    return 'NO'

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    OMOK_CHECK_NUM = 5
    omok_matrix = [input() for _ in range(N)]
    print(f'#{test_case} {omok(omok_matrix)}')