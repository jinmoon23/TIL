'''
맨 앞의 숫자를 맨 뒤로 보내는 작업을 spin_count번 했을 때, 수열의 맨 앞에 있는 숫자를 출력하는 프로그램

문제접근
1. from collections import deque
2. popleft() 및 append()를 spin_count 만큼 반복
3. 반복 후 가장 앞의 인덱스의 값을 반환
'''

import sys
from collections import deque
sys.stdin = open("5097_input.txt", "r")

def spin(q,spin_count):
    for i in range(spin_count):
        first_elem = q.popleft()
        q.append(first_elem)
    return q.popleft()

T = int(input())
for test_case in range(1, T + 1):
    N,spin_count = map(int,input().split())
    number_list = list(map(int,input().split()))

    q = deque()
    for number in number_list:
        q.append(number)

    print(f'#{test_case} {spin(q,spin_count)}')