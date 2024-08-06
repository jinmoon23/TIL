import sys
sys.stdin = open('input.txt',encoding='UTF8')

def find_str(compare,original):
    i = 0 # original의 인덱스
    j = 0 # compare의 인덱스
    result = 0 # 리턴을 위한 변수

    while i < N: # original의 모든 인덱스값을 탐색하기 위함
        if compare[j] == original[i]:
            i += 1
            j += 1
            if j == M: # 같은 글자가 원하는 만큼 있는 경우
                result += 1 # 리턴값을 하나 올려주고(count)
                j = 0 # 다시 처음부터 검색!
        else:
            i = i - j + 1
            j = 0
    return result

T = 10
for test_case in range(1,T+1):
    case_num = int(input())
    compare_str = input()
    original_str = input()
    N = len(original_str)
    M = len(compare_str)
    print(f'#{test_case} {find_str(compare_str,original_str)}')