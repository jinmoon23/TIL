'''
1. 짝이 맞춰지지 않은 경우
2. stack underflow 발생한 경우
3.
위 경우 -1을 리턴하고 그렇지 않으면 1을 리턴
'''


import sys
sys.stdin = open("input.txt", "r")

def find_brackets(brackets):
    bracket_couple_dict = {'(':')',')':'('}
    stack_of_bracket = []

    for bracket in brackets:
        stack_of_bracket.append(bracket) # input으로 받아온 brackets를 스택에 각각 저장

    while len(stack_of_bracket) > 0:
        bracket = stack_of_bracket.pop()
        for key in bracket_couple_dict:
            if bracket == key:
                if bracket_couple_dict[bracket] not in stack_of_bracket:
                    return -1 # early return
                stack_of_bracket.remove(bracket_couple_dict[key])

    return 1

T = int(input())
for test_case in range(1, T + 1):
    brackets = input()
    print(f'#{test_case} {find_brackets(brackets)}')