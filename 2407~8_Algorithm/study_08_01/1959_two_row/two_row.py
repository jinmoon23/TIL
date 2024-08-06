import sys
sys.stdin = open("input.txt", "r")

def solution(matrix):
    '''
    1. arr1의 0번 인덱스는 arr2의 0~2번 인덱스 값들과 만날 수 있다.
    2. arr1의 1번 인덱스는 arr2의 1~3번 인덱스 값들과 만날 수 있다.
    3. arr1의 2번 인덱스는 arr2의 2~4번 인덱스 값들과 만날 수 있다.
    4. arr1의 0~2번 인덱스와 arr2의 0~2번 인덱스와 곱한 값을 구하고
    '''
    compare_list = []
    if N < M:
        for i in range(N):
            for j in range(i,M-N+i+1):
                compare_list.append(matrix[0][i] * matrix[1][j])
    else:
        for i in range(M):
            for j in range(i,N-M+1+i):
                compare_list.append(matrix[1][i] * matrix[0][j])

    result_list = []
    if N<M:
        for l in range(M-N+1): # 연산횟수
            a = compare_list[l::M-N+1]
            result_list.append(sum(a))
    else:
        for l in range(N-M+1): # 연산횟수
            a = compare_list[l::N-M+1]
            result_list.append(sum(a))

    max_value = result_list[0]

    for m in range(len(result_list)):
        if max_value < result_list[m]:
            max_value = result_list[m]
    return max_value

T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    matrix = [arr1,arr2]
    print(f'#{test_case} {solution(matrix)}')


'''
가현님 코드리뷰
- elif는 else로도 동일하게 동작할 것 같습니다..? ><를 쓰신 이유도 궁금합니다.
'''