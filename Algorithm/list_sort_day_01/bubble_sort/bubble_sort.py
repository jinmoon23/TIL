# 각 구간의 끝 인덱스 i
# 각 구간에서 두 개씩 비교할 때 왼쪽 원소의 인덱스 j
# 왼쪽 원소가 더 크면 오른쪽 원소와 교환
import sys
sys.stdin = open('input.txt')
input_list = list(map(int,input().split()))

def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i): # len(arr)-2까지의 인덱스만 사용한다. 만약 그렇지 않은 경우 [j+1]에 indexerror가 발생
            if arr[j] > arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    print(arr)

print(bubble_sort(input_list))