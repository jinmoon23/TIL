'''
모든 정점을 깊이우선탐색하여 화면에 깊이 우선 탐색 경로를 출력하시오. 시작 정점을 1로 시작하시오.
정점 탐색시 숫자가 낮은 정점부터 방문한다.
예시 input: 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

1. input으로 받은 list를 각 정점이 어떤 정점과 연결되어있는지 식별이 가능한 형태의 리스트 또는 행렬로 변환한다.(아래는 리스트 형태로 변환)
2. start_list의 값을 바꿔가며 탐색하고 스택의 값이 모두 사라지면 탐색이 종료된 것이기 때문에 while 반복을 종료한다.
3. result_list의 모든 값을 str으로 mapping 후 '-'.join 메서드로 리턴한다.
'''

import sys
sys.stdin = open("input.txt", "r")

def find_dfs_path(point_arr):
    stack = []
    connected_list = [[] for _ in range(point_count + 1)] # 0번째 인덱스의 값은 빈 값이 와야하기 때문에 +1 해줘야 한다.
    visited = [0] * (point_count+1) # 방문여부를 기록하기위한 리스트
    start_point = 1
    result_list = []
    for i in range(line_count): # input으로 받은 포인트와 간선을 점간의 연결을 나타내도록 리스트로 변환하는 과정
        point, connected_point = point_arr[i*2],point_arr[i*2+1] # connected_list에서 point는 index를, connected_point는 연결된 정점을 나타낸다.
        connected_list[point].append(connected_point)
        connected_list[connected_point].append(point) # 1과2가 연결되어 있다면 2와1이 연결되어 있다고도 할 수 있다.
        # connected_list == [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[6,3]] -> (connected_list의 1번 인덱스)1번 포인트는 2,3번 포인트와 연결되어 있다.

    visited[1] = 1 # 첫 시작점 방문여부 기록

    stack.append(start_point)
    result_list.append(start_point)

    while True:
        for elem in connected_list[start_point]:
            if visited[elem] == 0:
                stack.append(elem)
                result_list.append(elem)
                visited[elem] = 1
                start_point = elem
                break # for문을 종료하고 while문을 다시 실행하면서 다시 for문을 실행 -> 핵심 아이디어 -> start_point가 변경된 이후이므로 다음 for 반복 시 그 값에서 시작되어 elem이 변동한다.
        else: # for문이 break 등으로 중간에 빠져나오지 않고 끝까지 실행 됐을 경우 else문이 실행되는 방식으로 진행됩니다.
            if stack: # 스택이 비어있지 않다면 아래 코드 실행
                start_point = stack.pop()
            else: # 스택이 비어있다면 탐색이 종료된 경우이므로 while문 종료
                break

    for_return = list(map(str,result_list))
    return '-'.join(for_return)


test_case = 1
point_count, line_count = map(int,input().split())
point_arr = list(map(int,input().split()))
print(f'#{test_case} {find_dfs_path(point_arr)}')