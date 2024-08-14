'''
"3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.
예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.
입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를
게임 규칙에 맞게 출력하는 프로그램을 작성하라.
박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.
'''

import sys
sys.stdin = open('input.txt')

def simple_369(number_list):
    result_list = []
    # for number in number_list:
    #     if number.isdigit() and number not in clab_dict.keys():
    #         result_list.append(number)
    #     elif int(number) < 10:
    #         if number in clab_dict.keys():
    #             result_list.append(clab_dict[number])
    #     elif int(number) >= 10:
    #         for char in number:
    #             if char in clab_dict.keys():
    #                 hyphens += '-'
    #         result_list.append(hyphens)
    #
    for number in number_list:
        if int(number) < 10:
            if number.isdigit() and number not in clab_dict.keys():
                result_list.append(number)
            if number in clab_dict.keys():
                result_list.append(clab_dict[number])
        elif int(number) >= 10:
            hyphens = ''
            for char in number:
                if number.isdigit():
                    result_list.append(number)
                    if char in clab_dict.keys():
                        result_list[-1] =


    return result_list

N = int(input())
number_list = []
for i in range(1,N+1):
    number_list.append(str(i))
clab_dict ={'3':'-', '6': '-', '9': '-'}
print(simple_369(number_list))