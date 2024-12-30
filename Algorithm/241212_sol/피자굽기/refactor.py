'''
화덕에 가장 마지막까지 남아있는 피자 번호를 알아내는 프로그램
피자는 1번위치에서 넣거나 뺄 수 있다. 1번에서 잠시 꺼내 치즈를 확인하고 다시 같은 자리에 넣을 수 있다.
화덕을 한 바퀴 돌 때 녹지않은 치즈의 양은 반으로 줄어든다. 이전 치즈의 양을 C라고 하면 다시 꺼냈을 때 C//2로 줄어든다.
치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자를 순서대로 넣는다.

1. q에 [피자번호,치즈양]을 피자판 수 만큼 넣는다.
2. q의 길이가 피자판 수와 같아지면
'''

import sys

sys.stdin = open('5099_input.txt')
from collections import deque

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 동시에 구울 수 있는 수 N / 피자 개수 M
    c = list(map(int, input().split()))  # 각 피자의 치즈양
    numbered_p = [[] for _ in range(M)]  # 피자의 번호와 각 피자의 치즈양이 하나의 인덱스 값([ , ]형태)에 포함된 리스트

    for index, elem in enumerate(c):
        numbered_p[index].append(index)
        numbered_p[index].append(elem)

    q = deque()
    # 조리가 완료된 피자를 빼낸 후 새로운 피자를 넣기 위한 변수
    k = 0
    # 완료된 피자가 완료 순서대로 쌓이는 리스트
    answer = []
    while k < M:
        # 화덕이 돌아가는 순서를 표현하기 위해 insert 사용
        q.insert(0, numbered_p[k])
        k += 1
        if len(q) == N:
            while q and q[0][1] != 0:
                poped = q.pop()
                poped[1] = poped[1] // 2
                q.insert(0, poped)
                if q[0][1] == 0:
                    answer.append(q.popleft())
                    q.insert(0, numbered_p[k])
                    k += 1
    print(f'#{tc}', answer[-1][0] + 1)
