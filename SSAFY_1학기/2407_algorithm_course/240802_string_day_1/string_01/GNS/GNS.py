# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아
# 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
# 입력으로 받아온 문자열을 정수로 변환 후 정렬
    # 'SVN'의 경우 '7'로 변환 -> ord('7')를 통해 ASCII 정수로 변환 -> 이 상태에서 정렬
# 정렬이 완료된 리스트의 순서대로 다시 문자열로 변환 후 리턴
    # [48,48,48,48+3,48+6,48+9]의 경우 chr(48)을 통해 '0'으로 변환 -> 이후 'ZRO'로 변환

import sys
sys.stdin = open('input.txt')

test_case = int(input())
for tc in range(1,test_case+1):
    test_case_num, test_case_len = input().split() # test_case_len은 단어의 갯수임!
    str_arr = input().split()
    integer_list = list(range(10))

