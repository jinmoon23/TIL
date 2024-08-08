'''
숫자는 스택에 넣는다.
연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
‘.’은 스택에서 숫자를 꺼내 출력한다.

Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.

피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
나눗셈의 경우 항상 나누어 떨어진다.

코드
출력
4 2 / .
2
4 3 - .
1

'''

import sys
sys.stdin = open("4874_input.txt", "r")

def forth(str_list):
    stack = []
    result_integer_list = []
    for string in str_list:
        if string.isdigit():
            stack.append(string)
        elif string == '.':
            return result_integer
        else:
            if stack:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                operator = string
                stack.append(calculator(num1,num2,string))
            else:
                pass



def calculator(num1,num2,operator):
    if operator == add:
        return num2 + num1
    elif operator == sub:
        return num2 - num1
    elif operator == multiple:
        return num2 * num1
    elif operator == divide:
        return num2 / num1


T = int(input())
for test_case in range(1, T + 1):
    str_list = input().split()
    add = '+'
    sub = '-'
    multiple = '*'
    divide = '/'

    print(f'#{test_case} {forth(str_list)}')