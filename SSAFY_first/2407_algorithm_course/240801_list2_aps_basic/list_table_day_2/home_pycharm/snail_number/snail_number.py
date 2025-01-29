# 달팽이 숫자
# 3을 입력받으면 3x3 행렬을 만든다.
#
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # NxN 행렬 만들기
    test_list = list(range(1,N*N+1))