'''
예비 후보지는 8개의 방향 중 사진을 찍을 수 있는 방향이 4방향 이상인 지점으로 정하려고 한다.
예비 후보지의 수를 알아내는 프로그램
착륙 지점을 중심으로 주변 8개 구역을 대상으로 착륙지점보다 높이가 낮은 구역의 사진을 찍을 수 있다.
'''


import sys
sys.stdin = open("input.txt", "r")

def find_point(matrix):
    dxy = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]] # 왼쪽 위부터 중심지의 왼쪽까지 시계방향으로 delta 설정
    result_count = 0
    for i in range(N):
        for j in range(M):
            point_count = 0
            for dx,dy in dxy:
                nx = i + dx
                ny = j + dy
                if nx<0 or ny<0 or nx>=N or ny>=M: continue
                if matrix[i][j] > matrix[nx][ny]:
                    point_count += 1
            if point_count >= 4:
                result_count += 1
    return result_count


T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{test_case} {find_point(matrix)}')