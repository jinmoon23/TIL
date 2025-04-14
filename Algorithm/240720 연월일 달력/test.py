t = int(input())

def check(test_list, i):
    result_str = ''.join(test_list) # '01010101'

    year_str = result_str[:4] # '0101'
    month_str = result_str[4:6] # '01'
    day_str = result_str[6:8] # '01'

    month_int = int(''.join(month_str)) # 01
    day_int = int(''.join(day_str)) # 01

    if month_int > 12 or day_int > 31 or month_int == 0 or day_int == 0:
        return f'#{i} -1' 
    elif month_int == 2 and day_int > 28:
        return f'#{i} -1'
    elif month_int == 4 or month_int == 6 or month_int == 9 or month_int == 11 and day_int > 30:
        return f'#{i} -1'
    else:
        return f'#{i} {year_str}/{month_str}/{day_str}'

for i in range(1,t+1):
    test_case_list = input().split() # ['01010101']
    print(check(test_case_list, i))


