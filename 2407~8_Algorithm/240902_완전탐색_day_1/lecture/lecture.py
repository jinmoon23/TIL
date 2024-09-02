# for i in range(1,4):
#     for j in range(1,4):
#         print(i,j,sep=' ')
#         # 1 1
#         # 1 2
#         # 1 3
#         # 2 1
#         # 2 2
#         # 2 3
#         # 3 1
#         # 3 2
#         # 3 3
# 1. 종료조건
# 2. 다음 재귀 호출 전
# 3. 재귀 호출
# 4. 호출하고 돌아왔을 때
# def KFC(x):
#     # 종료조건
#     if x > 5:
#         return
#     # 다음 재귀 호출 전
#     print(x)
#     # 재귀 호출
#     KFC(x+1)
#     # 호출하고 돌아왔을 때
#     print(x)
# KFC(0)

'''
순열
1. 중복없이
2. 순서를 고려하지 않고
3. 나열

중복순열
1. 중복이 가능하고
2. 순서를 고려하지 않고
3. 나열
'''

path = []
used = [0] * 7
def KFC(level):
    # 1. 종료조건
    if level == 3:
        print(*path)
        return
    # 2. 다음 재귀호출 전
    for i in range(1,7):
        # if i in path: continue -> 중복제거된 순열 생성 시 / 이 코드 주석처리하면 중복순열
        # 또한 시간복잡도가 O(len(path)) 이기 때문에 터질 수 있다!
        if used[i] == 1: continue

        # 2.1 경로 기록 + 방문기록
        used[i] = 1
        path.append(i)

        # 2.2 다음 재귀 호출
        KFC(level+1)

        # 2.3 돌아왔을 때 + 방문삭제
        path.pop()
        used[i] = 0

KFC(0)