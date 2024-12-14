
import sys
sys.stdin = open('algo1_sample_in.txt')


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(input())

    # 대칭 구간 없는 경우 1, 기본값 1 세팅
    max_v = 1
    # 절반 나눠서
    for i in range(1, N//2+1):
        cnt = 0
        # 작은 구간까지 탐색
        for j in range(1, i+1):
            # 좌우 같으면
            if arr[i+j] == arr[i-j]:
                # 글자수 저장
                cnt = 1+2*j
            # 좌우 안같으면 바로 break
            else:
                break
        # 글자수 최대 값 바로바로 저장
        if max_v < cnt:
            max_v = cnt
    print(f'#{tc} {max_v}')
