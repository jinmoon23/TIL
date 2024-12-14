from libs._bridge import init, submit, close
from collections import deque

NICKNAME = '부울경1반_최진문'
game_data = init(NICKNAME)

# if문으로 접근. 예외 처리가 사실상 불가능했다.
# 입력 데이터 분류
char_to_int = {'U': 0, 'R': 1, 'D': 2, 'L': 3}
map_data = [[]]  # 맵 정보. 예) map_data[0][1] - [0, 1]의 지형/지물
allies = {}  # 아군 정보. 예) allies['A'] - 플레이어 본인의 정보
enemies = {}  # 적군 정보. 예) enemies['X'] - 적 포탑의 정보
codes = []  # 주어진 암호문. 예) codes[0] - 첫 번째 암호문
visited = [[0]*100 for _ in range(100)]
# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    # 입력 데이터를 행으로 나누기
    game_data_rows = game_data.split('\n')
    row_index = 0

    # 첫 번째 행 데이터 읽기
    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])  # 맵의 세로 크기
    map_width = int(header[1])  # 맵의 가로 크기
    num_of_allies = int(header[2])  # 아군의 수
    num_of_enemies = int(header[3])  # 적군의 수
    num_of_codes = int(header[4])  # 암호문의 수
    row_index += 1

    # 기존의 맵 정보를 초기화하고 다시 읽어오기
    map_data.clear()
    map_data.extend([[ '' for c in range(map_width)] for r in range(map_height)])
    for i in range(0, map_height):
        col = game_data_rows[row_index + i].split(' ')
        for j in range(0, map_width):
            map_data[i][j] = col[j]
    row_index += map_height
    

    # 기존의 아군 정보를 초기화하고 다시 읽어오기
    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    # 기존의 적군 정보를 초기화하고 다시 읽어오기
    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    # 기존의 암호문 정보를 초기화하고 다시 읽어오기
    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i])
    
# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:
    # 자기 차례가 되어 받은 게임정보를 파싱
    print(f'----입력데이터----\n{game_data}\n----------------')
    parse_data(game_data)
    # visited = [[0]*len(map_data) for _ in range(len(map_data))]
    
    # 파싱한 데이터를 화면에 출력하여 확인
    print(f'\n[맵 정보] ({len(map_data)} x {len(map_data[0])})')
    for i in range(len(map_data)):
        for j in range(len(map_data[i])):
            print(f'{map_data[i][j]} ', end='')
        print()
    c_dir = ''
    print(f'\n[아군 정보] (아군 수: {len(allies)})')
    for k, v in allies.items():
        if k == 'A':
            c_dir += v[1]
            print(f'A (내 탱크) - 체력: {v[0]}, 방향: {v[1]}, 보유한 일반 포탄: {v[2]}개, 보유한 대전차 포탄: {v[3]}개')
        elif k == 'H':
            print(f'H (아군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (아군 탱크) - 체력: {v[0]}')

    print(f'\n[적군 정보] (적군 수: {len(allies)})')
    for k, v in enemies.items():
        if k == 'X':
            print(f'H (적군 포탑) - 체력: {v[0]}')
        else:
            print(f'{k} (적군 탱크) - 체력: {v[0]}')

    print(f'\n[암호문 정보] (암호문 수: {len(codes)})')
    for i in range(len(codes)):
        print(codes[i])


    # 탱크의 동작을 결정하기 위한 알고리즘을 구현하고 원하는 커맨드를 output 변수에 담기
    # 코드 구현 예시: '아래쪽으로 전진'하되, 아래쪽이 지나갈 수 있는 길이 아니라면 '오른쪽로 전진'하라

    output = ''
    # print(f'output 상태 확인: {output}')
    my_position = [-1, -1]
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            # 시작점을 발견한 경우
            if map_data[i][j] == 'A':
                my_position[0] = i
                my_position[1] = j
                # my_position = [i, j]로 변환되어 있음
                break
        if my_position[0] > 0: break
        
    dxy = [[0,-1],[-1,0],[0,1],[1,0]] # 좌 / 상 / 우 / 하
    
    cx, cy = my_position[0], my_position[1]
    q = deque([(cx,cy)])
    visited[cx][cy] = 1
    while q:
        cx, cy = q.popleft()
        for dx,dy in dxy:
            nx, ny = cx + dx, cy + dy
            if nx < 0 or ny < 0 or nx >= len(map_data) or ny >= len(map_data): continue
            if map_data[nx][ny] == 'R' or map_data[nx][ny] == 'W' or map_data[nx][ny] == 'T' or visited[nx][ny] == 1: continue
            # 이동이 가능한 경우(map_data에서 'G'인 경우)
            q.append((cx,cy))
            # 상단 이동이 가능한 경우
            if nx == cx - 1 and ny == cy:
                if c_dir == 'U':
                    output = 'A'
                    visited[nx][ny] = 1
                    if map_data[nx][ny] == 'X':
                        output = 'F'
                else:
                    output = 'U A'
                    visited[nx][ny] = 1
                    if map_data[nx][ny] == 'X':
                        output = 'F'                
            # 우측 이동이 가능한 경우
            if nx == cx and ny == cy + 1:
                if c_dir == 'R':
                    output = 'A'
                    visited[nx][ny] = 1
                    if map_data[nx][ny] == 'X':
                        output = 'F'                
                else:
                    output = 'R A'
                    visited[nx][ny] = 1
                    if map_data[nx][ny] == 'X':
                        output = 'F'                
            # 좌측 이동이 가능한 경우
            if nx == cx and ny == cy - 1:
                if c_dir == 'L':
                    output = 'A'
                    visited[nx][ny] = 1
                    if map_data[nx][ny] == 'X':
                        output = 'F'
                else:
                    output = 'L A'
                    visited[nx][ny] = 1
                    if map_data[nx][ny] == 'X':
                        output = 'F'
            # 하단 이동이 가능한 경우
            if nx == cx + 1 and ny == cy:
                if c_dir == 'D':
                    output = 'A'
                    visited[nx][ny] = 1
                    if map_data[nx][ny] == 'X':
                        output = 'F'
                else:
                    output = 'D A'
                    visited[nx][ny] = 1
                    if map_data[nx][ny] == 'X':
                        output = 'F'
    # def bfs(row,col):
    #     global output
    #     dxy = [[0,-1],[-1,0],[0,1],[1,0]] # 좌 / 상 / 우 / 하
    #     q = deque([(row,col)])
    #     visited[row][col] = 1
    #     while q:
    #         print(q)
    #         row, col= q.popleft()
    #         for dx,dy in dxy:
    #             nx, ny = row + dx, col + dy
    #             if nx < 0 or ny < 0 or nx >= len(map_data) or ny >= len(map_data): continue
    #             if visited[nx][ny] == 1: continue
    #             if map_data[nx][ny] == 'R' or map_data[nx][ny] == 'W' or map_data[nx][ny] == 'T': continue
    #             q.append((nx,ny))
    #             visited[nx][ny] = 1
    #             if map_data[nx][ny] == 'X': return 1
    #             # # 상단에 대한 이동이 가능한 경우 커맨드 추가
    #             # if nx == row -1 and ny == col: 
    #             #     output += 'U A '
    #             # elif nx == row and ny == col +1:
    #             #     output += 'R A '
    #             # elif nx == row + 1 and ny == col:
    #             #     output += 'D A '
    #             # else:
    #             #     output += 'L A '
    # # def contol(row,col):
    # #     global output
    # #     dxy = [[0,-1],[-1,0],[0,1],[1,0]] # 좌 / 상 / 우 / 하                
    # print(bfs(my_position[0],my_position[1]))        
    
    
    # if my_position[0] < len(map_data) - 1 and map_data[my_position[0] + 1][my_position[1]] == 'G':
    #     output = 'D A'
    # else:
    #     output = 'R A'

    # while 문의 끝에는 다음 코드가 필수로 존재하여야 함
    # output에 담긴 값은 submit 함수를 통해 배틀싸피 메인 프로그램에 전달
    game_data = submit(output)
    # game_data = submit(input())


# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()