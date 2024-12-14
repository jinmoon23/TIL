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

T = int(input())
for _ in range(1,T+1):
    N,M = map(int,input().split()) # 동시에 구울 수 있는 수 N / 피자 개수 M
    c = list(map(int,input().split())) # 각 피자의 치즈양
    numbered_p = [[] for _ in range(M)] # 피자의 번호와 각 피자의 치즈양이 하나의 인덱스 값에 포함된 리스트
    for index,elem in enumerate(c):
        numbered_p[index].append(index)
        numbered_p[index].append(elem)
    print(numbered_p)
    q = []
    for i in range(N):
        q.append(numbered_p[i])
    print(q)