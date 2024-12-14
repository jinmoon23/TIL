T = int(input())
for tc in range(1,T+1):
    s = input()
    N = len(s)
    result = 1
    for i in range(N//2):
        if s[i] != s[N-1-i]: # level의 경우 앞의 l과 뒤의 l을 비교하여 같지 않은 경우 회문이 아니기 때문에 result를 0으로 바꾸고 곧바로 연산을 종료한다.
            result = 0
            break
    print(f'#{tc} {result}')