import sys
sys.stdin = open("input.txt", "r")

def find_max_flower_powder(matrix):
    dxy = [[-1,0],[0,1],[1,0],[0,-1]] # 위 / 우측 / 아래 / 좌측
    # dx = [-1,0,1,0]
    # dy = [0,1,0,-1]
    compare_list = []
    for i in range(N):
        for j in range(M):
            dummy_list = []
            dummy_list.append(matrix[i][j])
            for dx,dy in dxy:
                nx = i + dx
                ny = j + dy
                if nx < 0 or ny < 0 or nx >= N or ny >= M: continue
                dummy_list.append(matrix[nx][ny])
            compare_list.append(sum(dummy_list))
    return max(compare_list)

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    print(f'#{test_case} {find_max_flower_powder(matrix)}')


'''
가현님 코드리뷰
- delta에 각각 0을 설정하는 아이디어 좋습니다!
- maxi랑 total 변수로 최대값 설정하는 아이디어 너무 좋네요! 전 빈 리스트 2개 만들었는데 가현님 접근이 더 빠른 실행이 가능할 것 같습니다. 
'''