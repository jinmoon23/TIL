'''
괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램
{( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다.
정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.

문제접근
1. 괄호를 키값쌍으로 갖는 딕셔너리를 생성한다.
2. 입력받은 문자열을 순회하며 열린 괄호를 발견하면 해당 열린 괄호를 스택에 담는다.
3. 계속 순회하다가 닫힌 괄호를 발견하면 스택을 확인하고 정상적인 짝인지 확인한다.
4. 만약 짝이 맞지 않으면 곧바로 0을 리턴한다.
5. 짝이 맞으면 계속 순회한다.
6. 모든 순회가 완료된 이후에 스택에 값이 남아있다면 제대로된 짝이 맞춰지지 않은 것이므로 0을 리턴한다.
7. 모든 순회가 완료된 이후 스택에 값이 없다면 모든 괄호가 짝을 이룬 것이므로 1을 리턴한다.

강사님 피드백
    - 스택에 pop하기 전에 항상 스택에 값이 있는지 확인해야 한다. 그렇지 않으면 런타임 오류가 발생함!
    - 예를들어 }{pr 같은 문자열이 입력된 경우 -1을 리턴하도록 해야함.
'''

import sys
sys.stdin = open("sample_input (2).txt", "r")

def bracket_inspection(string):
    stack = []
    result = 1

    for char in string:
        if char in bracket_dict.values(): # 해당 char이 ( 또는 { 같은 열린괄호라면 그 char을 스택에 담는다.
            stack.append(char)
        elif char in bracket_dict.keys(): # 해당 char이 ) 또는 } 같은 닫힌괄호라면 스택의 값(열린괄호)을 pop하고
            if not stack:
                return result - 1 # 런타임 오류를 방지하기 위해 stack에서 pop하기 전에 확인한다. 이 문제의 경우는 짝이 맞지 않는 경우를 의미하므로 -1을 리턴한다.
            if stack.pop() != bracket_dict[char]:
                return result - 1
    if stack:
        return result - 1
    return result


T = int(input())
for test_case in range(1, T + 1):
    inspection_string = input()
    bracket_dict = {'}':'{', ')':'('}
    print(f'#{test_case} {bracket_inspection(inspection_string)}')