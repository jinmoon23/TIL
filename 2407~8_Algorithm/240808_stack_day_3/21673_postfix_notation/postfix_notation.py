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
        elif not char.isdigit() and operation_dict[char] == 1: # + 또는 - 연산자면 곧바로 스택에 넣기
            if stack and operation_dict[stack[-1]] == 0:
                result.append(stack.pop())
                stack.append(char)
            else:
                stack.append(char)
        if not char.isdigit() and operation_dict[char] == 0: # * 또는 / 의 경우 같은 우선순위의 연산자가 스택에 없는 경우에만 스택에 넣기
            if not stack or operation_dict[stack[-1]] == 1: # 스택이 비어있다면 아래 코드 실행
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
    expression = input()
    print(postfix_notation(expression))
