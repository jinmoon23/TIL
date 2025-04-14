# 1234. [비밀번호]

'''
저는 이 문제 스택을 이용하여 풀었습니다.
스택이 비었으면 문자 하나씩 넣어주고 문자열을 순회하면서
만약 해당 문자가 스택에 담긴 마지막요소와 같지않으면 pop해주는 원리 이용하였습니다.
중복 문자열이 다 삭제되고 스택에 남은 문자열에 대해서만 문자열만 추출하는 것입니다.
'''

import sys
sys.stdin = open("input-6.txt", "r")

def delete_repeat(password):  # 중복 문자열 삭제해주는 함수
    stack = []   # 문자열 담을 빈 스택

    for num in password:  # 문자열은 시퀀즈 자료형이기에 for문 사용 가능
        if not stack or stack[-1]!= num:  # 스택이 비었거나 탐색중인 해당 요소가 스택의 마지막요소와 같지 않으면
            stack.append(num)  # 스택에 추가
        else:   # 만약 문자열이 스택 마지막 요소와 같다면 pop
            stack.pop()
    return stack   # 포문 돌리고 나서 남은 문자열 스택 반환

for case in range(1, 11):
    N, password = input().split()
    res = delete_repeat(password)
    print(f'#{case} {"".join(res)}')   # 문자열이니 join사용하여 예쁘게 출력~