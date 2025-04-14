import sys
sys.stdin = open('input.txt')

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left, equal, right = [], [], []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            equal.append(arr[i])
        else:
            right.append(arr[i])
    return [*quick_sort(left), *equal, *quick_sort(right)]

def b_search(t, s, e):
    stack = []
    while s <= e:
        m = (s + e) // 2
        if sorted_A[m] == t:
            return 1  # 양쪽을 번갈아 선택하지 않아도 정답으로 인정
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            return 0  # 같은 방향으로 두 번 연속 탐색 -> 조건 불충족
        if t > sorted_A[m]:
            s = m + 1
            stack.append(1)
        else:
            e = m - 1
            stack.append(0)
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    sorted_A = sorted(A)

    cnt = 0
    for elem in B:
        if b_search(elem, 0, len(sorted_A) - 1):
            cnt += 1

    print(f'#{tc} {cnt}')
