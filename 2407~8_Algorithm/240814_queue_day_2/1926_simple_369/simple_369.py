'''
"3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.
예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.
입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를
게임 규칙에 맞게 출력하는 프로그램을 작성하라.
박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.

문제접근
1. 입력으로 들어오는 숫자(str)가 10보다 작은 경우
    1-1. 3이나 6이나 9의 경우 -로 변환하여 result_list에 담는다.
    1-2. 그에 해당하지 않는 경우 그대로 result_list에 담는다.
2. 입력으로 들어오는 숫자(str)가 10보다 같거나 큰 경우
    2-1. for문을 통해 3이나 6이나 9가 포함되어 있는지 확인한다.
    2-2. 포함되어 있다면 -로 변환하여 담는다.
    2-3. 만약 2번 포함되어 있다면(ex, 33) --로 변환하여 담는다.

첫번째 elif 이하 코드 설명
예를들어 10의 경우 1과 0을 확인하는 과정을 거친다. 1과 0 모두 조건을 충족하지 않기 때문에 hyphens는 여전히 ''인 상태를 유지한다.
이후에 만나는 if문에서 else를 타게되고 해당하는 number를 result_list에 담으며 다음 반복으로 넘어간다.

예를들어 13의 경우 1과 3을 확인하는 과정을 거친다. 1은 조건을 충족하지 않지만 3은 조건을 충족하기 때문에 hyphens에 '-'를 추가한다.
for char 반복이 마무리된 후 if문을 만나고 hyphens 변수에 '-'이 저장되어 있으므로 else문을 거치지 않고 result_list에 해당 hyphens를 담으며 다음 반복으로 넘어간다.

33의 경우 1과 3 모두 조건을 충족하므로 hyphens 변수에 '--'가 저장된다. 이후 else문을 거치지 않고 result_list에 해당 hyphens를 담으며 다음 반복으로 넘어간다.
'''

import sys
sys.stdin = open('input.txt')
def simple_369(number_list):
    result_list = []

    for number in number_list:
        if int(number) < 10:
            if number.isdigit() and number not in clab_dict.keys():
                result_list.append(number)
            if number in clab_dict.keys():
                result_list.append(clab_dict[number])
        elif int(number) >= 10:
            hyphens = ''
            for char in number:
                if char in clab_dict.keys():
                    hyphens += '-'
            if hyphens == '-' or hyphens == '--':
                result_list.append(hyphens)
            else:
                result_list.append(number)

    return result_list

N = int(input())
number_list = []
for i in range(1, N + 1):
    number_list.append(str(i))
clab_dict = {'3': '-', '6': '-', '9': '-'}
print(*simple_369(number_list))
