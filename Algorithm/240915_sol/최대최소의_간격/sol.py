import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    min_v = [10,0]
    max_v = [0,0]

    for i,num in enumerate(arr):
        # 최소값은 가장 좌측의 인덱스 값을 추출하기 위해 부등호에 등호를 붙이지 않았고
        if min_v[0] > num:
            min_v[0] = num
            min_v[1] = i
        # 최대값은 가장 우측의 인덱스 값을 추출하기 위해 부등호에 등호를 붙임
        elif max_v[0] <= num:
            max_v[0] = num
            max_v[1] = i

    result = max_v[1]-min_v[1]
    # abs 메서드 없이 절대값 도출
    if result < 0:
        result = -result

    print(f'#{tc} {result}')