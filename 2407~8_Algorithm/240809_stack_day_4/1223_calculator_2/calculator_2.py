'''
문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
예를 들어
“3+4+5*6+7”
라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
"34+56*+7+"
변환된 식을 계산하면 44를 얻을 수 있다.
문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.
'''

import sys
sys.stdin = open("input.txt", "r")

def add_multiple_calculator(right,left,operator):
    if operator == '*':
        return int(left) * int(right)
    else:
        return int(left) + int(right)

def converter(expression):
    stack = []
    opeation_list = []
    for string in expression:
        if string.isdigit():
            opeation_list.append(string)
        elif not string.isdigit() and operator_order_dict[string] == 1 and "*" not in stack:
            stack.append(string)
        elif not string.isdigit() and operator_order_dict[string] == 1 and '*' in stack:
            while stack:
                right = opeation_list.pop()
                left = opeation_list.pop()
                opeator = stack.pop()
                opeation_list.append(add_multiple_calculator(right,left,opeator))
            stack.append(string)
        elif not string.isdigit() and operator_order_dict[string] == 0:
            stack.append(string)
    else:
        while stack:
            right = opeation_list.pop()
            left = opeation_list.pop()
            opeator = stack.pop()
            opeation_list.append(add_multiple_calculator(right, left, opeator))
        result = opeation_list.pop()
        return result

T = 10
for test_case in range(1, T + 1):
    input_str_len = int(input())
    input_str = input()
    operator_order_dict = {'+': 1, '*': 0}
    print(f'#{test_case} {converter(input_str)}')

