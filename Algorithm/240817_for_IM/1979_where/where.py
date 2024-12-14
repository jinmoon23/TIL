'''
N X N 크기의 단어 퍼즐을 만들려고 한다. 입력으로 단어 퍼즐의 모양이 주어진다.
주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라.

문제접근
1. 오로지 딱 맞는 경우에만 적합하다고 인정됨
2. 행에 접근해서 확인
3. 열에 접근해서 확인
4. 가능한 행렬 인덱스값 확인 후 카운팅
5. 카운팅 리턴
'''

import sys
sys.stdin = open("input (2).txt", "r")

def where(mat):
    cnt_lst = []
    for row in mat:
        if row.count(1) < K: continue
        for i in range(N):
            k = 0
            cnt = 0
            while i+k < N:
                if row[i+k] == 1:
                    cnt += 1
                    k += 1
                else:
                    cnt = 0
                    break
            if i+k < N and cnt == K and row[i-1] == 0 and row[i+K] == 0:
                cnt_lst.append(cnt)

    for i in range(N):
        for j in range(N):
            if i < j:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for row in mat:
        if row.count(1) < K: continue
        for i in range(N):
            k = 0
            cnt = 0
            while i+k < N:
                if row[i+k] == 1:
                    cnt += 1
                    k += 1
                else:
                    cnt = 0
                    break
            if cnt == K:
                cnt_lst.append(cnt)

    return len(cnt_lst)

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int,input().split()) # N 정방행렬길이 / K 단어의 길이
    puzzle = [list(map(int,input().split())) for _ in range(N)] # 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0 으로 주어진다.
    print(f'#{test_case} {where(puzzle)}')
