import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    # N: 컨테이너수 , M: 트럭수
    N, M = map(int, input().split())
    # N개의 화물의 무게 - 큰거 부터 정렬
    weight_lst = sorted(list(map(int, input().split())), reverse=True)
    # M개의 트럭 적재용량 - 큰거 부터 정렬
    truck_lst = sorted(list(map(int, input().split())), reverse=True)

    # 화물 담을 리스트
    move_lst = [0] * N

    # 화물이 트럭에 들어가는지 확인
    for i in range(M):
        j = 0
        while j < len(weight_lst):
            # 트럭보다 화물 무게가 작으면
            if truck_lst[i] >= weight_lst[j]:
                # 화물 담기
                move_lst[i] = weight_lst.pop(j)
                break
            j += 1

    print(f'#{tc} {sum(move_lst)}')