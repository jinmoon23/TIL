'''
파스칼의 삼각형
'''
import sys

sys.stdin = open('input.txt')

"""
재귀를 활용해서 구현 
시간복잡도:  O(N * 2^N )
"""

# row, col 이 주어졌을 때, 이전 row와 col을 구해가면서 현재 row, col을 구하는 재귀함수
def pascal_triangle(row, col):
    # 첫 번째 열이거나 마지막 열인 경우
    # 기저 조건, 재귀가 끝나는 지점
    if col == 0 or col == row:
        return 1

    # 재귀적으로 위 두 값을 더함
    return pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc}')

    for i in range(N):
        row = []
        for j in range(i + 1):
            row.append(str(pascal_triangle(i, j)))
        print(' '.join(row))

# 추가적인 코드는 깃랩참조