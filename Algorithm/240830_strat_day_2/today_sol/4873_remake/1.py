'''
원겸이는 문자열을 정리하는 게임을 하려고 한다.
문자열에서 같은 문자가 두 개 이상 연속된다면, 그 문자를 모두 제거하고 그 만큼의 점수를 얻는다.
한 번 정리를 한 이후에 다시 연속된 문자가 있다면, 다시 제거할 수 있다.
또한 정리 이후에 두개 이상의 연속하는 문자가 있을 경우 연속한 문자의 길이만큼 점수를 추가로 얻는다.
만약 연속하는 문자가 여러쌍일 경우, 모두 계산한다.
원겸이는 몇점을 얻을까?

다음은 XAAYBBBCDDCZD에서 반복문자를 지우는 경우의 예이다.

XAAYBBBCDDCZD에서 반복문자 AA, BBB, DD를 지우고 각각 2, 3, 2점을 얻는다. 그리고 X Y C CZD를 잇는다.
XYCCZD에서 반복문자 CC를 지우고 2점을 얻는다. 그리고 XY ZD를 잇는다.
XYZD는 반복문자가 없고 XYZ가 연속되므로 3점을 얻는다.
총점 12점을 리턴한다.


[입력]
첫 줄에 테스트 케이스 개수 T가 주어진다.  1 ≤ T ≤ 50
다음 줄부터 테스트 케이스의 별로 길이가 1000이내인 문자열이 주어진다.

[출력]
#과 1번부터인 테스트케이스 번호, 빈칸에 이어 답을 출력한다.

'''

import sys
sys.stdin = open('sample_input.txt')


def remove_repeat_ch(password):  # 반복문자 지우기
    score = 0
    stack = []
    cnt = 1
    for ch in password:
        if not stack or stack[-1][0] != ch:
            cnt = 1
            stack.append([ch, cnt])
        else:
            stack[-1][1] += cnt

   # [['X', 1], ['A', 2], ['Y', 1], ['B', 3], ['C', 1], ['D', 2], ['C', 1], ['Z', 1], ['D', 1]]

    word = ''
    for li in stack:
        if li[-1] >= 2:
            score += li[-1]
        else:
            word+= li[0]

    return score, word   # (7, 'XYCCZD')

def continuous_password(password):   # 연속문자 탐색 함수
    cnt = 1
    total = 0

    res = list(map(lambda ch : ord(ch), password))   # ord 문자열을 숫자로 바꿔주는 내장함수

    for i in range(1, len(res)):
        if res[i] == res[i - 1] + 1:
            cnt += 1
        else:
            if cnt > 1:
                total += cnt
            cnt = 1

    if cnt > 1:
        total += cnt

    return total


T = int(input())

for case in range(1, T+1):
    password = input()   # XAAYBBBCDDCZD
    ans = 0

    while True:
        score, password = remove_repeat_ch(password)
        ans+= score   # 전체 점수
        if score == 0:   # 점수가 0이란건 repeat되는게 없다는 뜻 반복문 탈출
            break

    print(continuous_password(password))

    print(f'#{case} {ans+continuous_password(password)}')

