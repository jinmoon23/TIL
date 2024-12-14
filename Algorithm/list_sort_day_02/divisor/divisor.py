import sys
sys.stdin = open('input.txt')

test_case = int(input())
verify_list = [2,3,5,7,11]

def find_divisor(num, i):
    result_list = []
    while num != 1: # 20 != 0
        for elem in verify_list: # 순서대로 2,3,5,7,11을 elem에 대입
            if num % elem == 0: # 20이 2 또는 3 또는 5 또는 7 또는 11로 나눠질 경우
                num = num // elem # 나눠진 이후의 값을 재할당 -> 이 경우 10이됨
                result_list.append(elem) # 나누는데 성공한 elem을 임의로 설정한 list에 담아줌 -> 이 경우 2가 들어감
    return f'#{i} {result_list.count(2)} {result_list.count(3)} {result_list.count(5)} {result_list.count(7)} {result_list.count(11)}' # list에서 2,3,5,7,11의 갯수를 factor에 담아 리턴

for i in range(1, test_case + 1):
    test_num = int(input())
    print(find_divisor(test_num, i)) # 예를들어 20이 input으로 들어온 경우