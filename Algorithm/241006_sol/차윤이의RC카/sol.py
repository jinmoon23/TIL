'''
'G' : RC카가 이동 가능한 땅
'T' : RC카가 이동이 불가능한 나무
'X' : 현재 RC카의 위치
'Y' : RC카를 이동 시키고자 하는 위치

RC카의 조종기로는 아래의 동작들을 할 수 있다.
'A' : 앞으로 이동 - 나무가 있는 곳이나 필드를 벗어나는 경우에는 아무 일도 일어나지 않는다.
      (RC카가 망가지는것을 방지하고자 장애물 판단 시스템이 탑재되었다.)
'L' : 현재 바라보고 있는 방향에서 왼쪽으로 90도 회전
'R' : 현재 바라보고 있는 방향에서 오른쪽으로 90도 회전

차윤이는 RC카를 항상 위를 바라보는 방향으로 부터 조종을 시작한다.
차윤이가 RC카를 조종한 커맨드가 주어졌을 때,  목적지에 도달 할 수 있는지 구하라.
목적지에 도달 할 수 있는지 구하라.
커맨드를 전부 실행 후 목적지에 도달했는지를 확인해야 함에 유의
'''

import sys
sys.stdin = open('sample_input.txt')
dir_R = [[1,1],[1,-1],[-1,-1],[-1,1]] # 1회 / 2회 / 3회 / 4회
dir_L = [[1,-1],[1,1],[-1,1],[-1,-1]] # 1회 / 2회 / 3회 / 4회
dxy = [[0,-1],[-1,0],[0,1],[1,0]] # 좌 / 상 / 우 / 하

def control_car(row,col):
    current_row, current_col = row-1, col
    for c, control in command:
        for char in control:
            if char == 'R':
                current_row, current_col = row + dxy[2][0], col + dxy[2][1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    field = [input() for _ in range(N)]
    control_cnt = int(input())
    command = [input().split() for _ in range(control_cnt)]
    # command_dict = {
    #     'A':
    # }
    for i, row in enumerate(field):
        for j, char in enumerate(row):
            if char == 'X':
                res = control_car(i,j)