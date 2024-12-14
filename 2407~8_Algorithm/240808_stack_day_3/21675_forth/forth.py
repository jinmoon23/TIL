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
    for string in str_list:
        if string.isdigit(): # 숫자면 일단 스택에 저장
            stack.append(string)
        elif string == '.': # '.'을 식별한 경우 모든 연산이 완료된 경우이므로 result_integer에 값 저장 후 리턴
            if str_list.index(string) != len(str_list)-1: # '.'이 중간에 식별된 경우 error early return
                return 'error'
            elif len(stack) > 1: # 마지막에 '.'이 발견되었지만 stack에 2개 이상의 값이 있다면 error early return
                return 'error'
            result = stack.pop()
            return result
        else: # 연산자인 경우
            if len(stack) >= 2:
                right = stack.pop()
                left = stack.pop()
                stack.append(calculator(right,left,string))
            elif len(stack) < 2:
                return 'error'

def calculator(right,left,string):
    if string == '+':
        return int(left) + int(right)
    elif string == '-':
        return int(left) - int(right)
    elif string == '*':
        return int(left) * int(right)
    elif string == '/':
        return int(left) // int(right)

T = int(input())
for test_case in range(1, T + 1):
    # str_list = ['10','2','3','5','6','7','4','+','*','.']
    str_list = input().split()
    print(f'#{test_case} {forth(str_list)}')