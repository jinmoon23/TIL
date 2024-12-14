import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    block = input()
    cnt = 0
    result = 0

    for char in block:
        if char == '1':
            cnt += 1
            if result < cnt:
                result = cnt
        else:
            cnt = 0

    print(f'#{tc} {result}')