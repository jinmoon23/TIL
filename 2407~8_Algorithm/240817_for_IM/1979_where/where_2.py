'''
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

문제접근
1. 각 행에서 1의 수를 count 후 리스트에 모두 담는다.
2. 이 때 주의할 점은 1 1 1 0 1 과 같은 행의 경우 리스트에 3과 1이 담겨야 한다는 점.
3. 이후 리스트에서 K와 동일한 값의 수를 리턴한다.

간단한 이해(5, 3)
0 0 1 1 1
1 1 1 1 0
0 0 1 0 0
0 1 1 1 1
1 1 1 0 1
내가 원하는 리스트의 값은 아래와 같다.
[3, 4, 1, 4, 3, 1]
이와 같은 리스트가 의미가 있는 이유는 (7,3) 입력에서 아래와 같은 행이 존재할 경우
1 1 1 0 1 1 1
0을 기준으로 왼쪽의 3칸과 오른쪽의 3칸은 정답이 될 칸인데 [3, 3] 이 아닌 [6]으로 인식하게 되면 내가 원하는 정답이 도출되지 않기 때문.
'''

import sys
sys.stdin = open("input (2).txt", "r")

def where(mat):
    dummy_list = []
    for i in range(N):
        cnt = 0
        if mat[i].count(1) < K: continue # 조건에 부합하지 않는 경우 early return
        for j in range(N):
            if mat[i][j] == 1:
                cnt += 1
            # 0을 만난 경우
            else:
                # 세고있던 cnt에 값이 있으면 그 값을 리스트에 저장
                if cnt != 0:
                    dummy_list.append(cnt)
                # cnt를 초기화 함으로써 연속성 보장
                cnt = 0
        # 7 3 & 1 1 1 0 1 1 1 같은 경우 마지막 3개의 1 1 1도 정답이 될 수 있지만 리스트에 저장되지 않는 문제 방지
        if cnt != 0:
            dummy_list.append(cnt)

    # 행렬 전치
    for i in range(N):
        for j in range(N):
            if i < j:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # 세로행에 대해서도 동일한 동작 진행
    for i in range(N):
        cnt = 0
        if mat[i].count(1) < K: continue
        for j in range(N):
            if mat[i][j] == 1:
                cnt += 1
            else:
                if cnt != 0:
                    dummy_list.append(cnt)
                cnt = 0
        if cnt != 0:
            dummy_list.append(cnt)

    return dummy_list.count(K)


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split()) # N 정방행렬길이 / K 단어의 길이
    puzzle = [list(map(int,input().split())) for _ in range(N)] # 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.
    print(f'#{test_case} {where(puzzle)}')
