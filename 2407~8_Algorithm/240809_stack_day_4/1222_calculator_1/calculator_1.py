'''
계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성
문자열 계산식을 구성하는 연산자는 + 하나뿐이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.
'''
import sys
sys.stdin = open("input.txt", "r")

def add_calculator(right,left,operator):
    if operator == '+':
        return int(left) + int(right)

def converter(expression):
    stack = []
    operation_list = []

    for string in expression:
        if string.isdigit():
            stack.append(string)
        elif not string.isdigit() and len(stack) < 2:
            operation_list.append(string)
        elif not string.isdigit() and len(stack) >= 2:
            right = stack.pop()
            left = stack.pop()
            operator = operation_list.pop()
            stack.append(add_calculator(right,left,operator))
            operation_list.append(string)
    else:
        if len(stack) == 1:
            result = stack.pop()
            return result
        else:
            right = stack.pop()
            left = stack.pop()
            operator = operation_list.pop()
            result = add_calculator(right,left,operator)
            return result

T = 10
for test_case in range(1, T + 1):
    input_str_len = int(input())
    input_str = input()
    print(f'#{test_case} {converter(input_str)}')
