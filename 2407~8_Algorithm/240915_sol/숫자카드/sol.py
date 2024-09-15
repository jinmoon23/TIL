'''
접근법
1. 동일한 숫자가 적힌 카드가 몇 장인지
2. 1의 카드가 가장 많은 숫자가 적힌 카드를 리턴
3. 만약 1의 카드 수가 모두 같다면 그 중 가장 큰 수가 적힌 카드를 리턴
'''

import sys
sys.stdin = open('sample_input.txt')

def find():
    # 중첩되는 카드가 있는 경우 가장 많은 카드의 수와 숫자를 리ㅌ
    max_v = [0,0]
    for key,value in card_dict.items():
        if max_v[1] < value:
            max_v[0], max_v[1] = key, value
    max_key = 0

    # 중첩되는 카드가 없는 경우 가장 큰 숫자를 가지는 카드를 리턴
    if max_v[1] == 1:
        for key in card_dict.keys():
            if max_key < key:
                max_key = key
        return [max_key, card_dict[max_key]]
    return max_v

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input()))
    card_dict = {}

    # {7: 3, 9: 2, 4: 2, 6: 1, 5: 1, 3: 1}의 형태로 나타내기 위한 코드블럭
    for num in arr:
        if num not in card_dict.keys():
            card_dict.setdefault(num,1)
        else:
            card_dict[num] += 1

    print(f'#{tc}', *find())