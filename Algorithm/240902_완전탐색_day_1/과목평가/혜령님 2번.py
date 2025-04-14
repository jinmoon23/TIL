import sys
sys.stdin = open('algo2_sample_in.txt')

def search(node):
    global cnt
    if node < 8:
        search(node*2)
        cnt += 1
        tree[cnt] = word[node]
        search(node*2+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    string = input()

    print(f'#{tc}', end=" ")
    for i in range(N):
        # ASCII 코드로 변환 후 8자리 2진수로 변환하기
        word = f"{ord(string[i]):08b}"
        tree = [0] * 8
        cnt = 0
        search(1)
        print("".join(list(map(str, tree[1:]))), end=" ")
    print()