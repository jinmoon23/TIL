import sys

sys.stdin = open('input.txt')
"""

"""
T = int(input())
# for _ in range(1):
for _ in range(T):
    tc, n = input().split()
    words = input().split()

    numbers = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    """
    numbers 변수를 앞에부터 순회를 한다. 
    ZRO -> 
    words 를 한 바퀴돌면서 ZRO 에 해당하는 친구들을 결과값에 추가한다. 
    ONE -> 
    words 를 한 바퀴돌면서 ONE에 해당하는 친구들을 결과값에 추가한다. 
    numbers 를 돌면 정렬 완료한 문자열을 구할 수 있껬죠 
    """
    result = ""
    for number in numbers:
        for word in words:
            if word == number:
                result += word + ' '

    print(tc)
    print(result)
