# print(bin(1<<5))
'''
조합
1. n 개 중 r개를
2. 순서없이
3. 나열
'''

# 1 1 1 ~ 6 6 6 / 주사위 경우의 수 전체 구하기

path = []

def dice(level, start):
    # 1. 종료조건 설정
    if level == 3:
        print(path)
        return

    for i in range(1,MAX_DICE+1):
        # 2. 재귀호출 전 동작
        path.append(i)
        # 3. 재귀호출
        dice(level+1, i)
        # 4. 재귀호출 후 동작
        path.pop()

MAX_DICE = 6
dice(0,0)