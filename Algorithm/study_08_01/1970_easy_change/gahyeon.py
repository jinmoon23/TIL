import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case}')
    inp = int(input())
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]  # 리스트로 편하게 돈의 위치에 접근

    mon = inp  # 돈을 mon함수에 저장(안하고 inp 써도 될듯)

    for i in range(len(lst)):
        count = mon // lst[i]
        mon = mon - (count * lst[i])  # 뺄셈 부분에서 챗GPT의 도움을 받음
        print(count, end=' ')
    else:
        print('')