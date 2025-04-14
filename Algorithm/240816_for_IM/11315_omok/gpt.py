import sys
sys.stdin = open("sample_input (2).txt", "r")
def omok(matrix, N):
    # 가로 검사
    for i in range(N):
        count = 0
        for j in range(N):
            if matrix[i][j] == 'o':
                count += 1
                if count == 5:
                    return "YES"
            else:
                count = 0

    # 세로 검사
    for j in range(N):
        count = 0
        for i in range(N):
            if matrix[i][j] == 'o':
                count += 1
                if count == 5:
                    return "YES"
            else:
                count = 0

    # 좌상 -> 우하 대각선 검사
    for i in range(N):
        for j in range(N):
            if i + 4 < N and j + 4 < N:  # 현재 위치에서 4칸 더 진행할 수 있는지 확인
                found = True
                for k in range(OMOK_CHECK_NUM):
                    if matrix[i + k][j + k] != 'o':
                        found = False
                        break
                if found:
                    return "YES"

    # 우상 -> 좌하 대각선 검사
    for i in range(N):
        for j in range(N):
            if i + 4 < N and j - 4 >= 0:  # 현재 위치에서 4칸 더 진행할 수 있는지 확인
                found = True
                for k in range(OMOK_CHECK_NUM):
                    if matrix[i + k][j - k] != 'o':
                        found = False
                        break
                if found:
                    return "YES"

    return "NO"

# 입력 및 테스트 케이스 처리
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    OMOK_CHECK_NUM = 5
    omok_matrix = [input().strip() for _ in range(N)]
    result = omok(omok_matrix, N)
    print(f'#{test_case} {result}')
