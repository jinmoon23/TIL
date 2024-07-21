t = int(input())

def average(list):
    sum_list = sum(list)
    division_num = sum_list // len(list)
    digit = sum_list % 10
    
    if sum_list % 10 == 0:
        return division_num
    else:
        if digit>= 5:
            return division_num+1
        else:
            return division_num

for i in range(1,t+1):
    test_num_list = list(map(int, input().split()))
    result = average(test_num_list)
    print(f'#{i} {result}')