import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())


def binary_tree(num, lst):
    if num > 7:  # 노드의 번호가 7 초과하면 return(비트가 7개만 들어가야하므로)
        return
    binary_tree(num * 2, lst)   # 왼쪽 자식 노드 번호
    pwd.append(str(lst[num]))   # 중위순회하며 읽는 비트를 pwd 리스트에 string 형태로 저장한다.
    binary_tree(num * 2 + 1, lst)   # 오른쪽 자식 노드 번호


for test_case in range(1, T + 1):
    N = int(input())    # N : 문자열의 길이
    str_lst = list(input())  # 문자열을 리스트로 입력받는다.

    for i in range(N):  # 입력받은 문자열을 ASCII 코드번호로 변환한다.
        str_lst[i] = ord(str_lst[i])    # 해당 인덱스의 문자열을 ASCII 코드번호로 변환
        change_bin = []  # 2진수로 변환한 값을 저장하기 위한 리스트
        while str_lst[i] >= 1:  # ASCII 코드번호를 2로 나눈 몫이 1보다 클 때까지 반복
            change_bin.append(str_lst[i] % 2)   # 리스트에 2로 나눈 나머지를 저장
            str_lst[i] //= 2
        while len(change_bin) < 8:  # 2진수로 변환한 값이 8자리가 될 때까지 0을 추가
            change_bin.append(0)
        str_lst[i] = change_bin[::-1]   # 위에서 변환한 2진수 값은 순서가 반대로 되어 있으므로 뒤집어서 원래 리스트 인덱스에 리스트로 재할당

    for i in range(N):  # 완전 이진 트리에 노드 번호대로 저장하고, 중위순회를 하여 암호를 만든다.
        pwd = []    # 비트를 모아 암호를 만들기 위한 리스트, 트리의 중위순회 순서대로 리스트에 저장
        binary_tree(1, str_lst[i])
        str_lst[i] = pwd    # 2진수로 된 리스트를 암호로 만든 리스트로 바꾼다.

    print(f'#{test_case}', end=' ')  # output 출력
    for i in range(N):
        print(''.join(str_lst[i]), end=' ')
    print()
