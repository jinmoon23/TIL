import sys

sys.stdin = open('input.txt')

numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
str_to_number = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

T = int(input())
for _ in range(1, T + 1):
    tc, n = input().split()
    words = input().split()
    max_value = 9

    # 인덱스는 1은 1부터 들어가기 때문에, +1 의 여유공간을 만들어야한다. 안그러면 터짐
    count_list = [0] * (max_value + 1)

    # 각 숫자(단어)의 출현 횟수를 세자
    for word in words:
        count_list[str_to_number[word]] += 1

    result = []
    # enumerate : idx 와 value를 반환하면서 순회하는 함수
    for i, c in enumerate(count_list):
        result.extend(([numbers[i]] * c))
    # print(result)
    print(" ".join(result))
