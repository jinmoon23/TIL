'''
5,000개의 버스 정류장 / 1에서 5,000까지 번호
버스 노선은 N개가 있는데, i번째 버스 노선은 번호가 Ai이상이고, Bi이하인 모든 정류장만을 다니는 버스 노선이다.
P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램

문제접근
1. 버스가 몇대인지 주어지고
2. 그 버스가 거쳐가는 버스정류장이 주어진다.
3. 버스정류장을 버스들이 몇 번 거쳐가는지를 계산하여 리턴한다.
4. N대의 버스가 입력으로 주어지면 이후의 입력 1 5는 1번 버스가 1~5번 정류장을 거쳐간다는 의미.
5. 1~5000번 까지의 버스정류장을 표현하기 위해 0을 값으로 가지는 배열을 만들고
6. 버스가 거쳐갈 때마다 그 값에 +1하여 재할당하면 반복이 종료된 후 원하는 배열이 형성된다.
'''

import sys
sys.stdin = open("s_input.txt", "r")

def bus_stop():
    stop_list = [0] * 5001

    for start,final in bus_path: # 각각의 버스가 정류하는 정류장의 시작과 끝을 받아온다.
        stops = number_generator(start, final) # 3 7의 경우 [3,4,5,6,7]로 변환한다.
        for index, stop in enumerate(stops):
            if stop in bus_stop_list: # 정류장번호가 input으로 받아온 값과 동일하면 정류하는지를 표시하는 stop_list에 정류장번호를 인덱스로하여 저장한다.
                stop_list[stop] += 1

    result_list = []
    for stop in bus_stop_list:
        result_list.append(stop_list[stop])

    return result_list

def number_generator(start,final):
    return list(range(start,final+1))

T = int(input())
for test_case in range(1, T + 1):
    bus_count = int(input())
    bus_path = [list(map(int,input().split())) for _ in range(bus_count)]
    bus_stop_count = int(input())
    bus_stop_list = [int(input()) for _ in range(bus_stop_count)] # 버스정류장 번호를 리스트로 받아옴
    print(f'#{test_case}', *bus_stop())