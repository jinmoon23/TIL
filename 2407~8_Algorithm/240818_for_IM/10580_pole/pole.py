'''
전선들이 복잡하게 꼬여 있는 전봇대 두 개
N개의 팽팽한 전선으로 연결되어 있었다. 두 전선이 끝점이 같은 경우는 없으나, 교차하는 경우는 있다.
세 개 이상의 전선이 하나의 점에서 만나지 않는다고 가정하자. -> 이게 무슨말이지? 아 밑의 언급때문에 고려하지 않아도 됨.
모든 Ai는 서로 다르고, 모든 Bi 도 서로 다르다. (두 전선의 끝점이 같은 경우가 없기 때문이다.) -> 한 전봇대에 걸린 2개의 전선이 하나의 점에서 시작할 수는 없다는 말.
세 전선이 한 점에서 만나지 않게 입력이 주어진다.
총 몇 개의 교차점이 있을까?

풀이
1. 부등호가 엇갈리는 쌍을 찾아라!
2. 먼저 N개의 라인 중 2개를 뽑는 경우의 수를 모두 고려해야 겠다.
3. 조합을 사용해야 할 듯. -> N개 중 M개를 뽑는 경우 -> N!/(N-M)!*M!

조합을 구현하려니 너무 복잡해진다..
새로운 풀이
1. 열은 0과 1 뿐이므로(전봇대는 2개 뿐) 0과 1로 열에 접근한다.
2. 행을 순회한다.
3. 엇갈리는 부등호를 확인해야 하므로 쌍으로 확인을 진행.
'''
import sys
sys.stdin = open("input (2).txt", "r")

def find_intersect(mat):
    cnt = 0
    for i in range(N):
        # 0번째 행부터 입력으로 받아오는 모든 행을 검사할 수 있도록 2중 for문 구성
        for k in range(1,N):
            # 인덱스 에러를 방지 / 엇갈리는 부등호 확인 시 cnt += 1
            if i+k < N and mat[i][0] > mat[i+k][0] and mat[i][1] < mat[i+k][1]:
                cnt += 1
            elif i+k < N and mat[i][0] < mat[i+k][0] and mat[i][1] > mat[i+k][1]:
                cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) # 두 전봇대 간 연결되어 있는 전선의 수
    lines = [list(map(int,input().split())) for _ in range(N)] # 두 전봇대 사이에서 선들이 어떤 높이에서 서로 연결되어 있는지 담겨있는 리스트
    print(f'#{test_case} {find_intersect(lines)}')

