import sys
sys.stdin = open('input1.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    block = input()
    cnt = 0
    result = 0

    for i,char in enumerate(block):
        if char == '1':
            cnt += 1
            if i+1 < N and block[i+1] == '0':
                if result < cnt:
                    result = cnt
                    cnt = 0
            # 마지막 인덱스의 값이 '1'인 경우 위 조건문에 의해 포함되지 못하는 문제가 발생. 아래의 코드로 해결
            if result < cnt:
                result = cnt
    print(f'#{tc} {result}')