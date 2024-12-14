'''
벽에 걸린 칠판에 자석이 붙어있는 글자들을 붙이는 장난감을 가지고 놀고 있다
이 장난감에 있는 글자들은 영어 대문자 ‘A’부터 ‘Z’, 영어 소문자 ‘a’부터 ‘z’, 숫자 ‘0’부터 ‘9’이다.
칠판에 글자들을 수평으로 일렬로 붙여서 단어를 만든다.
심심해진 의석이는 칠판에 만들어진 다섯 개의 단어를 세로로 읽으려 한다.
세로로 읽을 때 해당 자리의 글자가 없으면, 읽지 않고 그 다음 글자를 계속 읽는다.
'''
import sys
sys.stdin = open("input.txt", "r")

def column_talk(matrix):
    dx = [0,1,2,3,4] # 현 위치 찍고 행 4번 내려가기
    result_list = []
    row_len_list = []

    for i in range(word_count):
        row_len_list.append(len(matrix[i])) # 가장 긴 row의 길이를 파악한다.

    for i in range(word_count):
        if len(matrix[i]) != max(row_len_list): # 가장 긴 row의 길이보다 짧은 row를 식별하고
            matrix[i] += [''] * (max(row_len_list)-len(matrix[i])) # 그 row에 가장 긴 row와의 길이 차이만큼 ''공백문자를 추가한다. -> 핵심 아이디어

    for j in range(max(row_len_list)):
            result = ''
            for elem in dx:
                result += matrix[elem][j]
            result_list.append(result)

    return ''.join(result_list)


T = int(input())
for test_case in range(1, T + 1):
    word_count = 5
    str_matrix = [list(input()) for _ in range(word_count)]
    print(f'#{test_case} {column_talk(str_matrix)}')