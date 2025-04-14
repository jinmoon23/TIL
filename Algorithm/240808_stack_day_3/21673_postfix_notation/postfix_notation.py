'''
중위표기법 -> 후위표기법
1. 중위표기법의 예시 2+((3*4)/5)
2. 후위표기법 변환 예시 234*5/+

변환과정
1. expression을 순회하며 연산자를 스택에 담는다. 우선순위가 0인 연산자가 스택에 동시에 쌓일 것으로 예상되는 경우
   현재 스택을 pop하고
'''

import sys
sys.stdin = open("input.txt", "r")

def postfix_notation(expresion):
    stack = []
    result = []
    operation_dict = {'+' : 1,
                      '-' : 1,
                      '*' : 0,
                      '/' : 0
    }
    for char in expresion:
        if char.isdigit(): # 피연산자면 result에 곧바로 넣기
            result.append(char)
        elif not char.isdigit() and operation_dict[char] == 1: # + 또는 - 연산자인 경우
            if stack and operation_dict[stack[-1]] == 0: # 스택에 값이 있고 그 스택이 우선순위가 빠른 연산자인 경우
                while stack:
                    result.append(stack.pop())
                stack.append(char)
            else:
                stack.append(char)
        if not char.isdigit() and operation_dict[char] == 0: # * 또는 / 의 경우
            if not stack or operation_dict[stack[-1]] == 1:
                stack.append(char)
            elif operation_dict[stack[-1]] == 0:
                result.append(stack.pop())
                stack.append(char)
    else:
        if stack:
            while stack:
                result.append(stack.pop())

    return ''.join(result)

T = int(input())
for test_case in range(1, T + 1):
    expression = '3+2*5-8/4'
    print(postfix_notation(expression))
