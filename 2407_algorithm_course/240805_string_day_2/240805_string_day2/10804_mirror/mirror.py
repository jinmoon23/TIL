'''
‘b’, ‘d’, ‘p’, ‘q’로 이루어진 문자열이 주어진다. 이 문자열을 거울에 비추면 어떤 문자열이 되는지 구하는 프로그램을 작성하라.
각 테스트 케이스의 첫 번째 줄에는 ‘b’, ‘d’, ‘p’, ‘q’만으로 이루어진 하나의 문자열이 주어진다.

1. bdppq | pqqbd -> b와d가 대응되고 p와q가 대응된다.
2. 인자로 받아온 문자열을 대응되는 문자열로 변환한다. enumerate 메서드를 활용해보자
3. 변환한 문자열을 리턴한다.
'''


import sys
sys.stdin = open("input.txt", "r")


def mirror(string):
    mirror_dict = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
    result = ''

    for char in string:
        for key in mirror_dict:
            if char == key:
                result += mirror_dict[key]
    result_mirror = reversed_string(result)
    return result_mirror

def reversed_string(string):
    result = ''
    for i in range(len(string)-1,-1,-1):
        result += string[i]
    return result

T = int(input())
for test_case in range(1, T + 1):
    test_str = input()
    print(f'#{test_case} {mirror(test_str)}')