'''
그는 무조건 예약제로만 손님을 받으며, 예약을 하려는 손님들은 진기의 까다로운 자격 검증에서 합격해야만 붕어빵을 맛 볼 자격을 얻는다.
그래서 오늘은 N명의 사람이 자격을 얻었다.
진기는 0초부터 붕어빵을 만들기 시작하며, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있다.
붕어빵이 완성되면 어떤 시간 지연도 없이 다음 붕어빵 만들기를 시작할 수 있다.
0초 이후에 손님들이 언제 도착하는지 주어지면,
모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 없는지 판별하는 프로그램을 작성하라.
'''

import sys
sys.stdin = open("input.txt", "r")

def check_serving(dem,sup):
    stock = 0
    # 재고를 담을 변수를 생성하고 수요/공급 리스트를 인덱스로 순회
    # 재고가 0보다 작아지면 제 시간에 공급하지 못한 것이므로 early return
    # if문에 걸리지 않고 for문이 종료된 경우 수요에 적절히 대응한 공급이므로 Possible return
    for i in range(len(dem)):
        stock += sup[i]
        stock -= dem[i]
        if stock < 0:
            return 'Impossible'
    return 'Possible'

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int,input().split()) # N 대기수 / M 초당 생산되는 붕어빵의 수 == K
    arrive_arr = list(map(int,input().split()))

    # 최초의 붕어빵이 생산되기 전에 손님이 오는 경우 early return
    if M > min(arrive_arr):
        print(f'#{test_case} Impossible')
        continue

    # 붕어빵 수요를 리스트로 표현, 인덱스는 초의 역할
    dem_lst = [0] * (max(arrive_arr)+1)
    for arrive in arrive_arr:
        dem_lst[arrive] += 1

    # 몇 번 생산해야 모든 예약 주문을 처리할 수 있는지 연산
    prod_num = 0
    if N % K == 0:
        prod_num += N//K
    else:
        prod_num += (N//K) + 1

    # 붕어빵 공급을 리스트로 표현, 인덱스는 초의 역할
    sup_lst = [0] * (max(arrive_arr)+1)
    for i in range(1,prod_num+1):
        if M*i >= len(sup_lst): continue
        sup_lst[M*i] += K

    print(f'#{test_case} {check_serving(dem_lst,sup_lst)}')