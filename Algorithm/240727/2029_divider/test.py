test_case = int(input())

def divider(num1,num2,i):
    quo = num1//num2
    rem = num1%num2
    return print(f'#{i} {quo} {rem}')

for i in range(1,test_case+1):
    a,b = map(int,input().split()) # split은 스페이스바 입력에 대응
    divider(a,b,i)