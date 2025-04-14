'''
버블 소팅으로 구현해보자.
'''
import sys
sys.stdin = open('input (2).txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    for i in range(N):
        for j in range(0,N-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    print(f'#{tc}', *arr)