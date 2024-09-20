# 0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아
# 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
# 입력으로 받아온 문자열을 정수로 변환 후 정렬
    # 'SVN'의 경우 '7'로 변환 -> ord('7')를 통해 ASCII 정수로 변환 -> 이 상태에서 정렬
# 정렬이 완료된 리스트의 순서대로 다시 문자열로 변환 후 리턴
    # [48,48,48,48+3,48+6,48+9]의 경우 chr(48)을 통해 '0'으로 변환 -> 이후 'ZRO'로 변환

import sys
sys.stdin = open('input.txt')

def conversion(str_list):
    str_number_list = []
    result_list = []

    for string in str_list:
        for key in input_dict:
            if key == string:
                str_number_list.append(input_dict[key]) # input받은 리스트를 dict의 키와 비교하여 같은 경우 dict의 값을 list에 append
    number_list = list(map(int,str_number_list)) # 정수로 변환
    number_list.sort() # 정렬 -> [0,0,0,0,1,1,1,1,2,2,2,2,2...]

    for number in number_list:
        for key in result_dict:
            if number == key:
                result_list.append(result_dict[key]) # result_dict의 키와 number_list의 값이 같으면 해당 dict의 값을 result_list에 append
    return ' '.join(result_list)

test_case = int(input())
for tc in range(1,test_case+1):
    test_case_num, test_case_len = input().split() # test_case_len은 단어의 갯수임!
    str_arr = input().split()
    input_dict = {'ZRO':'0','ONE':'1','TWO':'2','THR':'3', 'FOR':'4', "FIV":'5', "SIX":'6', "SVN":'7', "EGT":'8', "NIN":'9'}
    result_dict = {0:'ZRO',1:'ONE',2:'TWO',3:'THR',4:'FOR',5:'FIV',6:'SIX',7:'SVN',8:'EGT',9:'NIN'}

    print(test_case_num, conversion(str_arr))


