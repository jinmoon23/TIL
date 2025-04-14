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
    k = 1 # 인덱스 이동시키기 위한 변수

    for i in range(student_number):
        if gender_list[i] == 1: # 남학생이 조작하는 경우
            for j in range(1,len(switches_list)+1): # 스위치 번호
                if j % chances_list[i] == 0:
                    switches_list[j-1] = control_switch(switches_list[j-1])

        else: # 여학생이 조작하는 경우
            for j in range(1, len(switches_list) + 1): # 1~8번 까지의 스위치
                if j-1-k < 0 or j-1+k >= len(switches_list): continue
                if j == chances_list[i]:
                    if switches_list[j-1-k] != switches_list[j-1+k]:
                        switches_list[j-1] = control_switch(switches_list[j-1])
                        break
                    switches_list[j-1] = control_switch(switches_list[j-1])
                    while switches_list[j-1-k] == switches_list[j-1+k]:
                        if j-1-k < 0 or j-1+k >= len(switches_list): break
                        switches_list[j-1-k], switches_list[j-1+k] = control_switch(switches_list[j-1-k]), control_switch(switches_list[j-1+k])
                        k += 1

    if len(switches_list) > 20:
        for i in range(len(switches_list) // 20):

    return switches_list



def control_switch(switch):
    if switch == 0:
        return 1
    return 0



switch_number = int(input())
switches_list =list(map(int,input().split()))
student_number = int(input())
gender_list = []
chances_list = []
for i in range(student_number):
    gender, given_chances = map(int,input().split())
    gender_list.append(gender)
    chances_list.append(given_chances)

print(*switch_controlled(switches_list,student_number))

for i in range(1, student_number + 1):
    print(switches_list[i - 1], end=" ")
    if i % 20 == 0:
        print()
