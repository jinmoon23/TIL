import sys
sys.stdin = open("input.txt", "r")

def find_section_sum(arr):

    # for i in range(N-1):
    #     for j in range(N-1):
    #         if arr[j] > arr[j+1]:
    #             arr[j],arr[j+1] = arr[j+1],arr[j]
    for i in range(N-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j] #  버블소팅

    min_section = arr[:M]
    max_section = arr[N-M:]
    min_value = 0
    max_value = 0

    for element in min_section:
        min_value += element
    for element in max_section:
        max_value += element

    return max_value - min_value


T = int(input())
for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    print(f'#{test_case} {find_section_sum(arr)}')