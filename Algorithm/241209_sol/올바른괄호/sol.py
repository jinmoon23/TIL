# 1. 문자열 s를 순회
# 2. 순회 중 (를 만나면 스택에 넣고 )를 만나면 stack[-1] 값을 pop
# 2-1 만약 (없이 )가 온다면 올바르지 않은 괄호이므로 early return
# 3. 순회가 종료된 후 stack에 값이 있다면 false 아니라면 true

def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return False
    print(stack)
    if stack:
        return False
    else:
        return True