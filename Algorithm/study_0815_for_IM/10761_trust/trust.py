'''
서로 다른 복도에 가둬놓고, 실험을 진행
한 복도에는 1 이상 100 이하의 정수로 구분되는 100개의 버튼이 존재
버튼 K는 복도의 시작점에서 K미터 떨어져 있다.
매 1초마다, 로봇은 복도의 양 방향 중 하나로 1미터 걷거나, 자기 위치에 있는 버튼을 누르거나, 아무 것도 하지 않는다.
    - 복도의 양 방향은 앞과뒤를 의미한다.
    - 로봇은 1초마다 걷거나 / 누르거나 / 아무것도 하지 않거나 하는 행동을 취한다.
순서대로 버튼을 눌러야 함
테스트를 끝낼 수 있는 가장 빠른 시간을 리턴

1번 테스트케이스 분석 (4 B 2 O 1 O 2 B 4)
1. 배열의 가장 앞 인덱스값이 4이므로 두 로봇은 총 4번의 버튼 클릭을 위해 이동한다.
2. 로봇B는 자신이 최종적으로 4번 버튼까지 가야한다는 사실을 알고 있다.
3. 로봇O는 자신이 최종적으로 2번 버튼까지 가야한다는 사실을 알고 있다.
4. 1초, B는 2번 버튼 도착, O는 대기
5. 2초, B는 2번 버튼 누름, O는 대기
6. 3초, B는 3번 버튼 도착, O는 1번 버튼 누름
7. 4초, B는 4번 버튼 도착, O는 2번 버튼 도착
8. 5초, B는 대기, O는 2번 버튼 누름
6. 6초, B는 4번 버튼 누름, O는 대기

3번 테스트케이스 분석 (2 O 2 O 1)
1. 1초, B는 대기, O는 2번 버튼 도착
2. 2초, B는 대기, O는 2번 버튼 누름
3. 3초, B는 대기, O는 1번 버튼 도착
4. 4초, B는 대기, O는 1번 버튼 누름

동시에 버튼을 누를수는 없다고 했으니 2 B 3 O 3 같은 경우를 고려해야 한다.
1. 1초, B와O는 2번 버튼 도착
2. 2초, B와O는 3번 버튼 도착
3. 3초, 동시에 버튼을 누를 수 없고 순열의 순서대로 눌러야 하므로 B는 버튼을 누르고 O는 대기
4. 4초, B는 대기, O는 버튼 누름

문제접근
1. 인풋으로 받아온 리스트
'''

import sys
sys.stdin = open("input (1).txt", "r")

def min_time(arr,click_number):
    time_count = 0
    before_location_B = 1
    before_location_O = 1

    for i in range(1,len(arr),4):
        if arr[i] > arr[i+2]:








T = int(input())
for test_case in range(1, T + 1):
    BUTTON_NUMBER = 100
    visited_buttons_B = [0] * BUTTON_NUMBER
    visited_buttons_O = [0] * BUTTON_NUMBER
    have_to_arr = input().split()
    have_to_click = int(have_to_arr.pop(0))
    ROBOTS = ['B','O']
    print(f'#{test_case} {min_time(have_to_arr,have_to_click)}')