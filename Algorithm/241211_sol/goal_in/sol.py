'''
N개의 숫자로 구분되는 바구니
하나의 바구니에는 하나의 공만 넣을 수 있다.
N개의 바구니에 M번 공을 넣는다.
한 번 공을 넣을 때, 공을 넣을 바구니 범위를 정하고, 정한 바구니에 모두 같은 번호가 적혀있는 공을 넣는다.
만약, 바구니에 공이 이미 있는 경우에는 들어있는 공을 빼고, 새로 공을 넣는다. 공을 넣을 바구니는 연속되어 있어야 한다.
공을 어떻게 넣을지가 주어졌을 때, M번 공을 넣은 이후에 각 바구니에 어떤 공이 들어 있는지 구하는 프로그램을 작성
즉, 모든 공을 다 넣은 후에 각 바구니 몇 번 공이 들어가 있는지 구하라는 것.
'''

import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split())
container = [list(map(int,input().split())) for _ in range(M)]
# 인덱스를 활용할 것이기 때문에 1번째 부터 넣는 문제에 대응하기 위해 더미 0을 맨 앞에 추가
answer = [0 for _ in range(N+1)]
def sol():
    for i,j,k in container:
        for p in range(i,j+1):
            answer[p] = k
    # 최종적으로 더미0을 제거
    answer.pop(0)
    return answer

print(*sol())