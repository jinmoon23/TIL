'''
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오.
도착할 수 있으면 1, 아니면 0을 출력한다.
마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
0은 통로, 1은 벽, 2는 출발, 3은 도착
'''

import sys
sys.stdin = open("4875_input.txt", "r")




T = int(input())
for test_case in range(1, T + 1):
    maze_size = int(input())
    maze_matrix = [input().split() for _ in range(maze_size)]
    print(maze_matrix)