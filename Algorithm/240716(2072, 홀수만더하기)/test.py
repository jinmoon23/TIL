t = int(input())

def find_add(list):
    odd_list = []
    for value in list:
        if value % 2 != 0:
            odd_list.append(value)
    return sum(odd_list)


for i in range(1,t+1):
    test_num_list = list(map(int, input().split()))
    result = find_add(test_num_list)
    print(f'#{i} {result}')