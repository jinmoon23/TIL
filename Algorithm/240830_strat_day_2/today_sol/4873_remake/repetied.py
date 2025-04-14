import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    pwd = list(input())
    stack = []
    cnt = 0
    idx = []
    k = 1
    res = 0
    a_stack = []
    # 1차적으로 res 카운팅 및 stack 저장 / 2개를 초과하여 연속된 경우 고려 x
    for i,char in enumerate(pwd):
        if not stack or char != stack[-1]:
            stack.append(char)
        else:
            res += 1
            idx.append(i)
            stack.pop()
            res += 1
    # 2개를 초과하여 연속된 경우 고려 및 stack에서 제거
    if idx:
        for i in idx:
            if i+k >= len(pwd): continue
            if pwd[i] != pwd[i+k]: continue
            # 2개 초과해서 반복되는 문자열이 발견된 경우
            k += 1
            res += 1
            for j,char in enumerate(stack):
                if stack and char == pwd[i]:
                    stack.pop(j)
            if i+k >= len(pwd): continue
            while pwd[i] == pwd[i+k]:
                k += 1
                res += 1
                if stack:
                    stack.remove(pwd[i])
            k = 1
    # ascii로 변환 후 연속성 파악 및 res 카운팅
    if stack:
        for char in stack:
            if not a_stack:
                a_stack.append(ord(char))
                continue
            if stack and a_stack and a_stack[-1] +1 == ord(char):
                a_stack.append(ord(char))
    if a_stack:
        res += len(a_stack)
    print(f'#{tc} {res}')