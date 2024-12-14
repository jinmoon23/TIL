def switch_controlled(switches_list, student_number):
    for i in range(student_number):
        if gender_list[i] == 1:  # 남학생이 조작하는 경우
            for j in range(1, len(switches_list) + 1):  # 스위치 번호
                if j % chances_list[i] == 0:
                    switches_list[j - 1] = control_switch(switches_list[j - 1])

        else:  # 여학생이 조작하는 경우
            k = 1  # 여학생 조작 시 k 초기화
            check_value = chances_list[i]  # 비교를 시작하는 스위치 위치 저장
            switches_list[check_value - 1] = control_switch(switches_list[check_value - 1])  # 자기 자신은 항상 변경해줌!
            while check_value - 1 - k >= 0 and check_value - 1 + k < len(switches_list) and switches_list[check_value - 1 - k] == switches_list[check_value - 1 + k]:
                switches_list[check_value - 1 - k], switches_list[check_value - 1 + k] = control_switch(switches_list[check_value - 1 - k]), control_switch(switches_list[check_value - 1 + k])
                k += 1  # 더 멀리 이동해서 확인하기 위한 변수 설정

    return switches_list

def control_switch(switch):
    return 1 if switch == 0 else 0

switch_number = int(input())
switches_list = list(map(int, input().split()))
student_number = int(input())

gender_list = []
chances_list = []
for i in range(student_number):
    gender, given_chances = map(int, input().split())
    gender_list.append(gender)
    chances_list.append(given_chances)

res = switch_controlled(switches_list, student_number)
for i in range(1, switch_number + 1):
    print(res[i - 1], end=" ")
    if i % 20 == 0:
        print()
