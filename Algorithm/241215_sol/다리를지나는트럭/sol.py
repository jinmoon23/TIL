'''
트럭 여러대가 일차선 다리를 정해진 순으로 지나려고 한다.
모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지 알아내야 한다.

1. truck_weights 배열이 false가 될 때 까지 반복
2. count 변수 활용이 필요?
3. 다리가 견딜 수 있는 최대 무게를 고려하기 위한 배열 변수 필요
4.
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    wait_trucks = deque(truck_weights)
    trucks = len(wait_trucks)
    acrossed_bridge_lst = []
    cnt = 0
    cnt_lst = []
    for truck in wait_trucks:
        cnt_lst.append([0,truck])
    # weight check list
    onbridge_lst = deque()
    while len(acrossed_bridge_lst) != trucks:
        cnt_lst[cnt][0] += 1
        if wait_trucks:
            truck_weight = wait_trucks.popleft()
            if sum(onbridge_lst) <= weight:
                onbridge_lst.append(truck_weight)
                if sum(onbridge_lst) > weight:
                    overweigted_truck = onbridge_lst.pop()
                    wait_trucks.insert(0,overweigted_truck)
                else:
                    cnt_lst[cnt + 1][0] += 1
            if cnt_lst[cnt][0] == bridge_length:
                acrossed_truck = onbridge_lst.popleft()
                acrossed_bridge_lst.append(acrossed_truck)
                cnt += 1
        else:
            acrossed_truck = onbridge_lst.popleft()
            acrossed_bridge_lst.append(acrossed_truck)






print(solution(2,10,[7,4,5,6]))
# print(solution(100,100,[10]))
# print(solution(100,100,[10,10,10,10,10,10,10,10,10]))