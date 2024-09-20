t = int(input())

def compare(list):
    if list[0]>list[1]:
        return '>'
    elif list[0]<list[1]:
        return '<'
    else:
        return '='


for i in range(1,t+1):
    test_case_list = list(map(int, input().split()))
    result = compare(test_case_list)
    print(f'#{i} {result}')


