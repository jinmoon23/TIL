# 1961, 숫자배열회전
# 회전을 직접 구현할 것인가 유사한 회전을 표현할 것인가?
#

t = int(input())

for i in range(1,t+1):
    N = int(input())
    test_arr = [list(map(int,input().split())) for _ in range(N)]
    zero_arr = [[0]*N for _ in range(N)]

