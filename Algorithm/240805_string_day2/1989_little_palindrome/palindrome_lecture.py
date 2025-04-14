# T = int(input())
# for tc in range(1,T+1):
#     s = input()
#     N = len(s)
#     result = 1
#     for i in range(N//2):
#         if s[i] != s[N-1-i]: # level의 경우 앞의 l과 뒤의 l을 비교하여 같지 않은 경우 회문이 아니기 때문에 result를 0으로 바꾸고 곧바로 연산을 종료한다.
#             result = 0
#             break
#     print(f'#{tc} {result}')
#
#
import sys
sys.stdin = open('input.txt')

def find_palindrome(string):
    N = len(string)
    result = 1
    for i in range(N//2): # 핵심 아이디어 -> 회문이기 위해선 각 인덱스에 대응되는 값이 같아야 한다는 점을 이용.
        if string[i] != string[N-1-i]: # 0과 마지막인덱스 / 1과 마지막인덱스의 -1 인덱스 ... 비교
            result = 0
            return result
    return result

T = int(input())
for test_case in range(1, T + 1):
    test_str = input()
    print(f'#{test_case} {find_palindrome(test_str)}')