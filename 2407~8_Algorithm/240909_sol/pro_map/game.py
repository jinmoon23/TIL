'''
최대한 빨리 도착하는 것이 유리
동, 서, 남, 북 방향으로 한 칸씩 이동
캐릭터가 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return 하도록 solution 함수를 완성해주세요.
단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return 해주세요.
처음에 캐릭터는 게임 맵의 좌측 상단인 (1, 1) 위치에 있으며, 상대방 진영은 게임 맵의 우측 하단인 (n, m) 위치에 있습니다.
'''
import sys
from collections import deque
sys.stdin = open('input.txt')

def find_min_distance(start):
    q.append(start)
    # 시작점을 방문체크
    v[0][0] = 1
    # while을 탈출했지만 마지막 값이 변함이 없다는 말의 의미는 목적지를 탐색하지 못했다는 의미. -1을 리턴하도록 한다.
    v[N-1][M-1] = -1
    while q:
        i, j = q.popleft()
        dxy = [[0,1],[0,-1],[1,0],[-1,0]] # 오른쪽 / 왼쪽 / 아래 / 위
        for dx, dy in dxy:
            nx = i + dx
            ny = j + dy
            # 조건설정
            if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
            if v[nx][ny] >= 1: continue
            if maps[nx][ny] == 0: continue
            # 이동할 좌표값을 큐에 담는다.
            q.append((nx,ny))
            # 이동할 visited 매트릭스의 좌표값에 +1 한 값을 넣는다.
            # bfs로 탐색
            v[nx][ny] = v[i][j] + 1

    return v[N-1][M-1]
T = int(input())
for tc in range(T):
    N,M = map(int,input().split())
    maps = [list(map(int,input().split())) for _ in range(N)]
    v = [[0]*M for _ in range(N)]
    q = deque()
    print(find_min_distance((0,0)))
