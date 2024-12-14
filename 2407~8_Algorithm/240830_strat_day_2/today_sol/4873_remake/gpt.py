
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    pwd = list(input())
    stack = []
    res = 0

    i = 0
    while i < len(pwd):
        # 스택이 비었거나 현재 문자와 스택의 마지막 문자가 다를 경우 스택에 추가
        if not stack or pwd[i] != stack[-1]:
            stack.append(pwd[i])
            i += 1
        # 스택의 마지막 문자와 현재 문자가 동일한 경우 (2개 연속) -> 제거
        elif pwd[i] == stack[-1]:
            stack.pop()
            res += 1  # 점수 증가
            i += 1

    # 스택에 남은 문자들 중에서 연속된 알파벳 체크
    i = 0
    while i < len(stack) - 1:
        if ord(stack[i + 1]) == ord(stack[i]) + 1:
            res += 1
            i += 2  # 두 개 연속된 알파벳 제거 후 넘어가기
        else:
            i += 1

    print(f'#{tc} {res}')
