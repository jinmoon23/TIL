'''
첫 번째 숫자를 1 감소한 뒤, 맨 뒤로 보낸다.
다음 첫 번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫 번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음 수는 5를 감소한다.
이와 같은 작업을 한 사이클이라 한다.
숫자가 감소할 때 0보다 작아지는 경우 0으로 유지되며, 프로그램은 종료
이 때의 8자리의 숫자 값이 암호가 된다.

문제접근
1. from collections import deque -> 양쪽 끝에서 빠르게 추가와 삭제를 할 수 있는 리스트류 컨테이너, popleft() or append()
2. input으로 받은 q의 인덱스를 5번 순회하며 1~5의 값을 빼준다.
3. 2의 과정을 while 반복문으로 처리하며 q의 마지막 인덱스 값이 0이거나 더 작은 경우 0으로 처리하고 return으로 함수와 while 반복문을 마무리한다.
'''

import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def password_generator(q):
    while True:
        for i in range(CYCLE_NUMBER):
            dummy = q.popleft() - (i+1)
            q.append(dummy)
            if q[-1] <= 0:
                q[-1] = 0
                return q

T = 10
for test_case in range(1, T + 1):
    case = int(input())
    password_candidate = list(map(int,input().split()))
    q = deque()
    CYCLE_NUMBER = 5
    for number in password_candidate:
        q.append(number)
    print(f'#{test_case}',*password_generator(q))