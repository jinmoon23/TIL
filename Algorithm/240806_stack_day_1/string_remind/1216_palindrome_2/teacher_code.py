import sys
sys.stdin = open('input.txt')
import time
start_time = time.time()

# 문자열이 회문인지 확인하는 함수
def is_palindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1
    return True


# 문자열이 회문인지 확인하는 함수 (간단 버전, is_palindrome 함수와 동일하게 동작)
def is_palindrome_simple(string):
    return string == string[::-1]


# 가장 긴 회문을 찾는 함수
def find_longest_palindrome(matrix):
    # 0부터 100까지 값을 가지고, 가로 검사에서는 행, 세로 검사에서는 열 ( 0, 1, 2, 3, ..., 100)
    for i in range(N):
        # 긴 길이부터 검사를 진행함 ( 100, 99, 98, ..., 2 )
        # 긴 문자열부터 검사하면, 찾았을 때 바로 반환할 수 잇음
        for length in range(N, 1, -1):
            # 가로 검사에서는 열, 세로 검사에서는 행 ( length=100, start=0 // length=99, start= 0, 1, ... )
            for start in range(N - length + 1):
                # 가로 방향 검사
                if is_palindrome(matrix[i][start:start + length]):
                    return length  # 가장 긴 회문을 찾으면 즉시 반환

                # 세로 방향 검사 ( 세로로 인자를 가져와서 회문 검사 )
                column = []
                for j in range(start, start + length):
                    column.append(matrix[j][i])

                if is_palindrome(column):
                    return length

                # 세로로 슬라이싱 (리스트 컴프리헨션, 미세하지만 속도가 더 빠름)
                # if is_palindrome([matrix[j][i] for j in range(start, start + length)]):
                #     return length

    return 1  # 2글자 이상의 회문을 못 찾은 경우.


for test_case in range(1, 11):
    tc = int(input())
    N = 100
    matrix = [input() for _ in range(N)]

    result = find_longest_palindrome(matrix)
    print(f"#{tc} {result}")
end_time = time.time()

print(end_time-start_time)