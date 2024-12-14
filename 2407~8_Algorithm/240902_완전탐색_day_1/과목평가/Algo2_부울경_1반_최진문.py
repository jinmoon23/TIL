'''
이싸피는 영문자와 숫자를 완전이진트리를 이용해 암호화 하는 새로운 암호체계를 만들었다.
문자열은 영문자와 0-9까지의 숫자로만 구성되어있다.

접근법
1. 입력받은 문자열을 ord()로 변환 -> 65
2. 해당 10진수를 2진수로 변환
3. 2번의 2진수 중 가장 앞의 인덱스값을 제외하고 따로 저장
4. 3의 문자열의 가장 빠른 인덱스값부터 트리에 순서대로 저장
'''

import sys
sys.stdin = open('algo2_sample_in.txt')
def make_pwd(node):
    # 완전이진트리의 특성 이용한 종료조건설정
    if node > CANDIDATE_NUM:
        return
    make_pwd(node*2)
    # 중위순회
    pwd.append(tree[node])
    make_pwd(node*2+1)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    CANDIDATE_NUM = 7
    block = input()
    b_lst = []
    # 2진수로 변환
    for char in block:
        b_lst.append(bin(ord(char)))

    s_lst = []
    # 0b 제거
    for elem in b_lst:
        s_lst.append(elem[2:])
    tree = [0] * (CANDIDATE_NUM + 1)
    pwd = []
    result = []
    for elem in s_lst:
        for i,char in enumerate(elem,1):
            # 트리에 값 삽입
            tree[i] = int(char)
        # 재귀함수 호출
        make_pwd(1)
    else:
        for i in range(N):
            result.append(pwd[i*CANDIDATE_NUM:i*CANDIDATE_NUM+CANDIDATE_NUM])
    print(f'#{tc}', end=' ')
    for i in range(N):
        res = map(str,result[i])
        final = ''.join(res)
        print(final, end=' ')
    print()

