'''
전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램
종점에 도착할 수 없는 경우는 0을 출력
출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

테스트케이스 분석(3/10/5 [1,3,5,7,9])
1. 0번부터 10번까지 총 11개의 정류장
2. 0번부터 시작해 3번 정류장까지 충전없이 이동이 가능하고 3번에서 충전해야만 추가적인 이동이 가능함(1회)
3. 3번부터 6번 정류장까지 충전없이 이동이 가능하지만 6번 정류장에 충전기가 없기 때문에 그 3번과 6번 사이 정류장에서 충전해야 추가적인 이동이 가능함. 따라서 5번 정류장에서 충전실시(2회)
4. 5번부터 8번 정류장까지 충전없이 이동이 가능하지만 8번 정류장에 충전기가 없기 때문에 5번과 8번 사이 정류장에서 충전해야 추가적인 이동이 가능함. 따라서 7번 정류장에서 충전실시(3회)
5. 7번 정류장에서 10번 정류장까지 충전없이 이동이 가능하고 10번이 종점이기 때문에 함수종료. 3회 리턴

테스트케이스 분석(3/10/5 [1,3,7,8,9])
1. 0번부터 10번까지 총 11개의 정류장
2. 0번부터 시작해 3번 정류장까지 충전없이 이동이 가능하고 3번에서 충전해야만 추가적인 이동이 가능함(1회)
3. 3번부터 6번 정류장까지 충전없이 이동이 가능함. 하지만 6번 정류장에도 3번과 6번 정류장 사이에도 충전이 가능한 정류장이 없기 때문에 종점까지 이동이 불가능함.
4. 0 리턴
.
문제접근
1. 0부터 N을 포함하는 리스트 생성
2. 슬라이싱을 통해 탐색
3. in 메서드를 사용해 충전이 가능한 정류소인지 확인
4. i 변수를 통해 정류장 이동 구현
'''
import sys
sys.stdin = open("sample_input.txt", "r")

def min_charge(K,elec_M,stops):
    cnt = 0
    i = 1
    while True:
        slc = stops[i:i+K] # i를 계속적으로 변경해 정류장에 접근하기 위한 슬라이싱.
        for j in list(reversed(slc)): # 최대 운행가능거리에 딱 맞는 경우를 식별하기 위한 reversed 확인.
            if j in elec_M: # elec_M == [1,3,5,7,9] 즉, 슬라이싱 한 리스트 내부를 뒤에서 접근해 충전기가 있는 정류소인지 확인
                cnt += 1
                i = stops.index(j) + 1 # +1을 하는 이유는 확인했던 정류장을 중복해서 확인하지 않기 위함.
                if j + K >= N: # 이 경우는 종점이 i에서의 최대 운행거리보다 가깝거나 동일한 경우 추가적인 확인이 불필요하기 때문.
                    return cnt
                break
        else:
            cnt = 0
            return cnt

T = int(input())
for test_case in range(1, T + 1):
    K,N,M = map(int,input().split()) # 최대 이동가능 정류장 / 종점 / 충전기가 설치된 정류장 갯수
    elec_M = list(map(int,input().split()))
    stops = list(range(N+1)) # 슬라이싱을 통해 정류장을 구간별로 확인하기 위한 리스트 생성.
    print(f'#{test_case} {min_charge(K,elec_M,stops)}')