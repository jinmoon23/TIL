t = int(input())

def find(list):
    return max(list)

for i in range(1,t+1):
    test_case_list = list(map(int,input().split()))
    result = find(test_case_list)
    print(f'#{i} {result}')