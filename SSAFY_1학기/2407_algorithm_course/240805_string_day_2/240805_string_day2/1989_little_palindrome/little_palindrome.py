'''
"level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
회문이면 1을 출력하고, 아니라면 0을 출력

1. 인자로 받은 문자열을 뒤집어서 인자와 비교
2. 같으면 1을 출력, 아니라면 0을 출력
'''
import sys
sys.stdin = open('input.txt')

def find_palindrome(string):
    reversed_string = reverse_string(string)
    if reversed_string == string:
        return 1
    else:
        return 0

def reverse_string(string):
    reversed_string = ''
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

T = int(input())
for test_case in range(1, T + 1):
    test_str = input()
    print(f'#{test_case} {find_palindrome(test_str)}')