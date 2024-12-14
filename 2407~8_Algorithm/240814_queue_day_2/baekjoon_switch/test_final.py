'''
남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.
<그림 1>과 같은 상태에서 남학생이 3을 받았다면, 이 학생은 <그림 2>와 같이 3번, 6번 스위치의 상태를 바꾼다.

여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간을 찾아서,
그 구간에 속한 스위치의 상태를 모두 바꾼다.
이때 구간에 속한 스위치 개수는 항상 홀수가 된다.

스위치들의 마지막 상태를 출력하는 프로그램을 작성하시오.

문제접근
1. gender_list와 chances_list의 앞에서부터 스위치 조작이 시작된다.
'''

import sys
sys.stdin = open('input.txt')

def switch_controlled(switches_list,student_number):

    for i in range(student_number):
        if gender_list[i] == 1: # 남학생이 조작하는 경우
            for j in range(1,len(switches_list)+1): # 스위치 번호
                if j % chances_list[i] == 0:
                    switches_list[j-1] = control_switch(switches_list[j-1])

        else: # 여학생이 조작하는 경우
            k = 1  # 인덱스 이동시키기 위한 변수 -> 핵심입니다! 함수 가장 바깥에 위치시키면 다른 여학생(2번째 이후)의 경우 고려가 안됩니다.
            check_value = chances_list[i] # 비교를 시작하는 스위치 위치 저장
            switches_list[check_value - 1] = control_switch(switches_list[check_value - 1]) # 자기 자신은 항상 변경해줌!
            # 아래 while문의 올바른 설정이 내 접근의 핵심
            # 파이썬은 위에서 아래로, 왼쪽에서 오른쪽으로 코드를 해석하기 때문에 인덱스 에러관련 코드는 적절하게 배치해야 한다.
            # if check_value-1-k<0 or check_value-1+k>=len(switches_list) 를 while문의 가장 아래에 위치시켰는데 인덱스에러 발생. 아마 while문 위치에서 코드가 터지지 않았나 추측함.
            while check_value-1-k>=0 and check_value-1+k<len(switches_list) and switches_list[check_value-1-k] == switches_list[check_value-1+k]: # 자기 자신 양옆이 대칭(같은 값)이면 스위치 토글
                switches_list[check_value-1-k], switches_list[check_value-1+k] = control_switch(switches_list[check_value-1-k]), control_switch(switches_list[check_value-1+k])
                k+=1 # 더 멀리 이동해서 확인하기 위한 변수 설정

    return switches_list

def control_switch(switch):
    if switch == 0:
        return 1
    return 0

switch_number = int(input())
switches_list =list(map(int,input().split()))
student_number = int(input())

# 이 밑의 input값을 받는게 정말 힘들었음..
gender_list = []
chances_list = []
for i in range(student_number):
    gender, given_chances = map(int,input().split())
    gender_list.append(gender)
    chances_list.append(given_chances)

# 이런식으로 받으면 더 간편?
gender_given_list = [list(map(int,input().split())) for _ in range(student_number)]

# 강사님의 코드
# student_list = [list(map(int, input().split())) for _ in range(student_count)]

res = switch_controlled(switches_list,student_number)
for i in range(1, switch_number + 1):
    print(res[i - 1], end=" ")
    if i % 20 == 0:
        print()