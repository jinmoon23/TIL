import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())    # 배열의 길이
    num_lst = list(input())  # 2진수 배열
    max_sym = 0     # 최대 대칭 구간의 길이

    for i in range(N):
        sym = 1     # 대칭 구간의 길이를 계산할 변수
        j = 1   # 좌우로 늘어나는 인덱스의 길이
        while i - j >= 0 and i + j < N:  # 인덱스 범위 벗어나기 전까지 반복
            if num_lst[i - j] == num_lst[i + j]:    # 대칭이면
                sym += 2    # 대칭 길이 +2
                j += 1  # 늘어나는 인덱스 길이 +1
            else:   # 대칭이 아니면
                break   # 반복문(while) 탈출
        if max_sym <= sym:  # 최대 대칭 구간의 길이보다 방금 구한 대칭 구간의 길이가 더 크면
            max_sym = sym   # 최대 대칭 구간의 길이 교체

    print(f'#{test_case} {max_sym}')
