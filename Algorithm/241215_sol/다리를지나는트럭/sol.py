'''
트럭 여러대가 일차선 다리를 정해진 순으로 지나려고 한다.
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 한다.

1. truck_weights 배열이 false가 될 때 까지 반복
2. count 변수 활용이 필요?
3. 다리가 견딜 수 있는 최대 무게를 고려하기 위한 배열 변수 필요
4.
'''
from collections import deque
from os import access


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    across_bridge = []
    cnt = 0
    # weight check list
    wc_lst = deque()
    while cnt <= bridge_length or truck_weights:
        if sum(wc_lst) <= weight:
            cnt += 1
            if truck_weights:
                pl = truck_weights.popleft()
                if sum(wc_lst) + pl <= weight:
                    wc_lst.append(pl)
                else:
                    truck_weights.insert(0,pl)
        if cnt % bridge_length == 0:
            poped = wc_lst.popleft()
            across_bridge.append(poped)
            if not truck_weights and not wc_lst:
                break
    return cnt + 1

# print(solution(2,10,[7,4,5,6]))
# print(solution(100,100,[10]))
print(solution(10,100,[10,10,10,10,10,10,10,10,10]))