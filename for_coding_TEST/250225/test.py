# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    t_map = [[0] * n for _ in range(n)]
    
    row = 0
    for elem1 in arr1:
        b_elem1 = bin(elem1)[2:]
        while len(b_elem1) < n:
            b_elem1 = '0' + b_elem1
        # 다루기 쉬운 이진수로 변환
        for i, char in enumerate(b_elem1):
            t_map[row][i] += int(char)
        row += 1
    
    row = 0
    for elem2 in arr2:
        b_elem2 = bin(elem2)[2:]
        while len(b_elem2) < n:
            b_elem2 = '0' + b_elem2
        for i, char in enumerate(b_elem2):
            t_map[row][i] += int(char)
        row += 1
    # 여기까지 0과 0이 아닌 수로 t_map 2차원 행렬 정리됨
    result = []
    for i in range(n):
        for j in range(n):
            if t_map[i][j] == 0:
                t_map[i][j] = ' '
            else:
                t_map[i][j] = '#'
        result.append(''.join(t_map[i]))
    return result


print(solution(5,	[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))