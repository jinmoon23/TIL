'''
반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.
'''
import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    s = input() # ABCCB
    stack = []
    for char in s:
        if not stack or stack[-1] != char:
            stack.append(char)
        else:
            stack.pop()
    cnt = 0
    for char in stack:
        cnt += 1
    print(f'#{test_case} {cnt}')
