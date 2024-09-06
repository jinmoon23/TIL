'''
트럭당 한 개의 컨테이너를 운반 할 수 있고, 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어지고, A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행한다고 한다.
이때 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하는 프로그램을 만드시오.
화물을 싣지 못한 트럭이 있을 수도 있고, 남는 화물이 있을 수도 있다. 컨테이너를 한 개도 옮길 수 없는 경우 0을 출력한다.

'''

import sys
from collections import deque
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) # 물건의 수 / 트럭의 수 -> 3 / 2
    c_lst = sorted(list(map(int,input().split())), reverse=True) # 물건의 무게를 담은 리스트 / [1,5,3]
    dummy = sorted(list(map(int,input().split())), reverse=True) # 트럭의 최대적재무게 / [8,3]
    # popleft()를 활용해 사용이 완료된 트럭을 배제하기 위함
    m_lst = deque(dummy)

    res = 0

    for c in c_lst:
        for m in m_lst:
            # 컨테이너 무게가 트럭의 최대적재무게보다 작거나 같다면 적재가 가능
            if c <= m:
                res += c
                # 적재 완료 후 해당 트럭 계산에 배제
                m_lst.popleft()
                # 컨테이너의 적재 가능여부 더이상 판단하지 않아도 됨
                break
            # 내림차순 정렬되었기 때문에 앞에서 무게초과가 난다면 뒤를 더 보지않아도 된다.
            else:
                break

    print(f'#{tc} {res}')

