'''
주어진 100x100 평면 글자판에서 가로, 세로를 모두 보아 가장 긴 회문의 길이를 구하는 문제
글자 판은 무조건 정사각형으로 주어진다.
ABA도 회문이며, ABBA도 회문이다. A또한 길이 1짜리 회문이다. -> 절대 리턴값은 0이될 수 없다.

1.매트릭스의 모든 요소 순회
2. 기준요소의 좌우로 -i와i를 더한 인덱스의 값에 접근
3. 만약 i와-i 값에 접근 후 회문인지 확인 후 맞다면 기준요소와 i, -i 값도 함께 회문검사를 실시해야 함.
--- 위 접근은 검사해야 하는 요소가 4개인 경우(ABBA) 적용이 불가능함

1. 0행부터 99행까지, 가장 왼쪽의 요소부터 회문검사 실시 -> 1행당 (n)(n+1)/2번의 연산
2. 핵심로직 -> 모든 행의 0번 인덱스부터 n-1인덱스까지 회문검사 반복. 이 때 슬라이싱의 길이를 1씩 계속 늘려가는 것이 검사의 핵심.
'''

import sys
sys.stdin = open("input.txt", "r")
import time
start_time = time.time()

def find_max_len_palindrome(matrix):
    result_list = [] # 리턴값을 얻기위한 리스트
    string_list = [] # 가로 요소들의 회문조건을 체크하기 위한 리스트
    reversed_char_list = [] # 대각선을 기준으로 가로/세로를 뒤집기 위한 리스트
    reversed_string_list = [] # 세로 요소들의 회문조건을 체크하기 위한 리스트

    for row in matrix:
        for string in row:
            string_list.append(string) # input으로 받은 이중배열 내부의 통짜string을 써먹기 편하게 1차원배열 형태로 저장

    for i in range(len(string_list)):
        for string in string_list:
            reversed_char_list.append(string[i])
            if len(reversed_char_list) == matrix_size:
                dummy = ''.join(reversed_char_list)
                reversed_char_list.clear()
                reversed_string_list.append(dummy) # 대각선을 기준으로 가로/세로를 뒤집는 코드블럭

    for string in string_list:
        for i in range(len(string_list)):
            for j in range(len(string_list)):
                if j+1 < i: continue # 인덱스 에러를 방지
                slicing = string[i:j+1] # 회문이라면 적어도 1의 길이를 가져야 하기 때문
            # 만약 string[i:i+1]이 회문조건을 충족한다면 palin_len += 1 하고 (i+3)+1의 슬라이싱도 회문조건을 충족하는지 확인. 반복.
                if is_palindrome(slicing):
                    result_list.append(slicing) # 회문조건을 만족하는 경우 result_list에 그 슬라이싱을 저장

    for string in reversed_string_list:
        for i in range(len(reversed_string_list)):
            for j in range(len(reversed_string_list)):
                if j+1 < i: continue # 인덱스 에러를 방지
                slicing = string[i:j+1] # 회문이라면 적어도 1의 길이를 가져야 하기 때문
            # 만약 string[i:i+1]이 회문조건을 충족한다면 palin_len += 1 하고 (i+3)+1의 슬라이싱도 회문조건을 충족하는지 확인. 반복.
                if is_palindrome(slicing):
                    result_list.append(slicing) # 회문조건을 만족하는 경우 result_list에 그 슬라이싱을 저장

    result_len_list = [] # 회문조건을 만족하는 모든 경우의 슬라이싱의 길이를 저장

    for string in result_list:
        result_len_list.append(len(string))

    max_return_value = result_len_list[0] # 가장 큰 값을 찾기위한 코드블럭
    for length in result_len_list:
        if max_return_value < length:
            max_return_value = length

    return max_return_value

def is_palindrome(slicing):
    slicing_len = len(slicing)

    for i in range(slicing_len//2):
        if slicing[i] != slicing[slicing_len-1-i]:
            return False
    return True

T = 10
for i in range(1, T + 1):
    case = int(input())
    matrix_size = 100
    str_matrix = [list(input().split()) for _ in range(matrix_size)]
    print(f'#{case} {find_max_len_palindrome(str_matrix)}')


end_time = time.time()

print(end_time - start_time)