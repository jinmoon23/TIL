import sys
sys.stdin = open('input.txt')

N,M = map(int,input().split()) # 강의의 수 / CD의 수
arr = list(map(int,input().split())) # 각 강의의 크기
# 최초의 슬라이싱 합과 슬라이싱 이후의 리스트 -> 비교를 위함
sum_slc = []
slc = []
for i in range(0,N,M):
    slc.append(arr[i:i+M])
    sum_slc.append(sum(arr[i:i+M]))
new_current = 0
while True:
    current = max(sum_slc)
    c_index = sum_slc.index(current)
    # 가장 큰 값이 맨 왼쪽에 있는 경우
    if c_index == 0:
        sub = slc[c_index].pop(-1)
        sum_slc[c_index] = sum_slc[c_index] - sub
        sum_slc[c_index + 1] = sum_slc[c_index + 1] + sub
        slc[c_index + 1].insert(0, sub)
        new_current = max(sum_slc)
        # 만약 더 큰 값이 나오는 경우 연산을 계속해도 무한반복되므로 while 탈출
        if new_current > current:
            new_current = current
            break
        continue
    # 가장 큰 값이 맨 오른쪽에 있는 경우
    elif c_index == M-1:
        sub = slc[c_index].pop(0)
        sum_slc[c_index] = sum_slc[c_index] - sub
        sum_slc[c_index - 1] = sum_slc[c_index - 1] + sub
        slc[c_index - 1].append(sub)
        new_current = max(sum_slc)
        # 만약 더 큰 값이 나오는 경우 연산을 계속해도 무한반복되므로 while 탈출
        if new_current > current:
            new_current = current
            break
        continue
    # 가장 큰 값이 맨 왼쪽과 맨 오른쪽의 중간 부분에 존재하는 경우
    # 더 작은 값을 찾은 후 그 방향으로 연산
    dir_sum = min(sum_slc[c_index-1], sum_slc[c_index+1])
    # 더 작은 값이 오른쪽에 있는 경우
    if dir_sum == sum_slc[c_index+1]:
        sub = slc[c_index].pop(-1)
        sum_slc[c_index] = sum_slc[c_index] - sub
        sum_slc[c_index+1] = sum_slc[c_index+1] + sub
        slc[c_index+1].insert(0,sub)
        new_current = max(sum_slc)
        # 만약 더 큰 값이 나오는 경우 연산을 계속해도 무한반복되므로 while 탈출
        if new_current > current:
            new_current = current
            break
    # 더 작은 값이 왼쪽에 있는 경우
    else:
        sub = slc[c_index].pop(0)
        sum_slc[c_index] = sum_slc[c_index] - sub
        sum_slc[c_index - 1] = sum_slc[c_index - 1] + sub
        slc[c_index - 1].append(sub)
        new_current = max(sum_slc)
        # 만약 더 큰 값이 나오는 경우 연산을 계속해도 무한반복되므로 while 탈출
        if new_current > current:
            new_current = current
            break
print(new_current)