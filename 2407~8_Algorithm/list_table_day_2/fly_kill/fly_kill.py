# 0행의0열 값부터 전체 값에 순차적으로 접근
# 그 값 / 오른쪽 / 오른쪽 대각선 / 밑 값의 합을 구해서 result_list에 담기
# out of range indexError를 어떻게 처리할 것인가?
#
test_case = 10

for i in range(1,test_case+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

