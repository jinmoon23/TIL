'''
풍선이 M개씩 N개의 줄에 붙어있고
어떤 풍선을 터뜨리면 안에 든 종이 꽃가루 개수만큼 상하 좌우의 풍선이 추가로 터지게 되는 게임
꽃가루의 합 중 최대값을 출력하는 프로그램

문제접근
1. 행렬의 모든 값에 접근하기 위해 2중 for문 구성
2. 접근한 값을 터뜨려서 얻는 값을 변수에 저장
3. 접근한 값 만큼 상하좌우 이동하여 터뜨린 후 얻는 값을 변수에 저장
4. 최대값을 산정하기 위해 임의 생성한 변수에 3의 값을 append
5. 최대값 산정 및 리턴
'''
import sys
sys.stdin = open("input1.txt", "r")

def pop(matrix):
    result_list = []
    for i in range(row):
        for j in range(column):
            pop_count = 0
            dxy = [[-1,0],[1,0],[0,-1],[0,1]]
            pop_count += matrix[i][j] # 접근한 값을 터뜨려서 얻은 값 저장

            for dx,dy in dxy: # start delta
                nx = i + dx
                ny = j + dy
                for k in range(matrix[i][j]):
                    # if nx-k < 0 or nx+k >= row or ny-k < 0 or ny+k >= column: continue
                    if dx == 0 and dy == -1: # 좌 delta 접근 시
                        if ny-k < 0: continue
                        pop_count += matrix[nx][ny-k]
                    elif dx == 0 and dy == 1: # 우 delta 접근 시
                        if ny + k >= column: continue
                        pop_count += matrix[nx][ny+k]
                    elif dy == 0 and dx == -1: # 상 delta 접근 시
                        if nx-k < 0: continue
                        pop_count += matrix[nx-k][ny]
                    elif dy == 0 and dx == 1: # 하 delta 접근 시
                        if nx+k >= row: continue
                        pop_count += matrix[nx+k][ny]
            result_list.append(pop_count)

    max_value = result_list[0]
    for i in range(len(result_list)):
        if max_value < result_list[i]:
            max_value = result_list[i]

    return max_value




T = int(input())
for test_case in range(1, T + 1):
    row,column = map(int,input().split())
    game_matrix = [list(map(int,input().split())) for _ in range(row)]
    print(f'#{test_case} {pop(game_matrix)}')
