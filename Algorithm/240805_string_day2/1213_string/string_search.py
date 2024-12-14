'''
원본 문자열에서 일치하는 특정한 문자열의 개수를 반환하는 프로그램을 작성
Brute Force
- 비교 문자가 같으면 원본,비교 문자열 인덱스 모두 뒤로 한 칸씩 이동
- 비교 문자가 다르면 원본은 한 칸 앞으로 이동, 비교는 맨 처음 인덱스로 이동

'''
import sys
sys.stdin = open("input.txt", encoding='UTF8')

def search_str(find,original):
    # index를 아래와 같이 설정하는 것이 핵심 아이디어
    i = 0 # original의 인덱스
    j = 0 # find의 인덱스
    result = 0

    while i < N: # i가 original의 길이를 넘어서면 인덱스 에러가 발생함. 이를 방지하기 위함.
        if original[i] != find[j]:
            # 아래의 코드는 원본과 비교의 값이 다를 경우 실행됨
            i = i - j + 1
            j = 0
            continue
        i += 1
        j += 1
        if j == M:
            result += 1
            j = 0
            i = i - j + 1
    return result

T = 10
for test_case in range(1, T + 1):
    case = int(input())
    find = input()
    original = input()
    N = len(original)
    M = len(find)
    print(f'#{case} {search_str(find,original)}')