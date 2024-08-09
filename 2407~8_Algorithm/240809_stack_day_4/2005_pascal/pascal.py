'''
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.
'''
import sys
sys.stdin = open("input.txt", "r")

def pascal_triangle(size):
    pascal_matrix = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            pascal_matrix[i][0] = 1
            pascal_matrix[i][i] = 1
            if i >=2 and j > 0:
                pascal_matrix[i][j] = pascal_matrix[i-1][j-1] + pascal_matrix[i-1][j]

    for i in range(size):
        while 0 in pascal_matrix[i]:
            pascal_matrix[i].pop()
    # 이 위 코드까지 파스칼 삼각형 완성
    for i in range(size):
        while pascal_matrix[i]:

            print(pascal_matrix[i].pop(),end=' ')
        print()


T = int(input())
for test_case in range(1, T + 1):
    pascal_size = int(input())
    print(f'#{test_case}')
    print(f'{pascal_triangle(pascal_size)}')
